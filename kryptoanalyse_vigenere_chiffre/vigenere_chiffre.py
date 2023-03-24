def encrypt_tabelle(key, cleartext):
    """
    encrypt_tabelle verschlüsselt den übergebenen cleartext mit dem ebenfalls übergebenen Schlüssel.
        Zudem wird für den Schlüssel zur späteren Veranschaulichung in html eine Liste erstellt,
        welche die Schlüsselbuchstaben mit deren zur Entschlüsselung verwendeten Zahlenwert enthält.
        Für denselben Zweck wird auch für die Verschlüsselung eine Liste erstellt. Diese enthält jeweils die
        Klartextbuchstaben, deren Zahlenwert, die angewandten Schlüsselwerte, die Additionsergebnisse der
        beiden Zahlenwerte sowie die berechneten entschlüsselten Buchstaben
    :param key: der zur Entschlüsselung verwendete Schlüssel
    :param cleartext: der zu verschlüsselnde Text
    :return: key_list (die Schlüsselliste), encrypt_list (dei Verschlüsselungsliste) und der verschlüsselte Text
    """

    encrypt_list = []
    key_list = []
    keystand = 0
    ciphertext = ""

    # Iteration über die Schlüssellänge. Dabei werden die Buchstaben des Schlüssels mit deren
    # zur Entschlüsselung benötigten und hier berechneten Zahlenwert der Liste key_list hinzugefügt
    for _, value in enumerate(key):
        zahl = ord(value) - 97
        key_list.append([value, zahl])

    # Iteration über die Cleartextindexe
    for _, value in enumerate(cleartext):
        # Umwandlung des Buchstabens in eine Zahl
        zeichen = ord(value) - 97

        # Hier wird das betrachtete Zeichen des Klartextet mit dem Schlüsselzeichenwert, welcher sich in dem
        # gespeicherten Indexwert in key befindet, durch Addition der beiden Buchstabenwerte berechnet. Zudem werden
        # der verwendetet Schlüsselzeichenwert, der Klartextbuchstabe (als Zichen und Zahl) und der verschlüsselte
        # Buchstabe (ebenfalls als Zeichen und Zahl) in der Verschlüsselungsliste encrypt_list hinzugefügt
        keynumber = key_list[keystand][1]
        encryptnummer = (zeichen + keynumber) % 26
        encryptzeichen = chr(encryptnummer + 65)
        encrypt_list.append([value, zeichen, keynumber, encryptnummer, encryptzeichen])

        # keystand auf den nächsten Indexwert setzen und hinzufügen des verschlüsselten Buchstabens in ciphertext
        keystand += 1
        keystand = keystand % len(key_list)
        ciphertext += encryptzeichen

    return key_list, encrypt_list, ciphertext


def decrypt_tabelle(key, ciphertext):
    """
    decrypt_tabelle entschlüsselt den übergebenen ciphertext mit dem ebenfalls übergebenen Schlüssel.
    Zudem wird für den Schlüssel zur späteren Veranschaulichung in html eine Liste erstellt,
    welche die Schlüsselbuchstaben mit deren zur Entschlüsselung verwendeten Zahlenwert enthält.
    Für denselben Zweck wird auch für die Entschlüsselung eine Liste erstellt. Diese enthält jeweils die
    Klartextbuchstaben, deren Zahlenwert, der angewante Schlüsselwert, das Subtraktionsergebnis der beiden Zahlenwerte
    sowie den berechneten entschlüsselten Buchstaben
    :param key: der zur Entschlüsselung verwendete Schlüssel
    :param ciphertext: der zu entschlüsselnde Text
    :return: key_list, decrypt_list, cleartext
    """

    decrypt_list = []  # Liste für die Veranschaulichung der Entschlüsselung
    key_list = []  # Liste für die Veranschaulichung des Schlüssels
    keystand = 0  # speichert einen Index von key
    cleartext = ""  # enthält den entschlüsselten Text

    # Iteration über die Schlüssellänge. Dabei werden die Buchstaben des Schlüssels mit deren
    # zur Entschlüsselung benötigten und hier berechneten Zahlenwert der Liste key_list hinzugefügt
    for _, value in enumerate(key):
        zahl = ord(value) - 97
        key_list.append([value, zahl])

    # Iteration über den bereinigten ciphertext
    for _, value in enumerate(ciphertext):
        # Umwandlung des betrachteten Buchstabens in eine Zahl (zwischen 0 und 25)
        zeichen = ord(value) - 65

        # enthält den zur Entschlüsselung nötigen Schlüsselbuchstabenwert
        keynumber = key_list[keystand][1]

        # Berechnung des Wertes, des entschlüsselten Buchstabens
        decryptnummer = (zeichen - keynumber) % 26

        # Umwandlung des entschlüsselten Buchstabenwertes in den entschlüsselten Buchstaben
        decryptzeichen = chr(decryptnummer + 97)

        # Hinzufügen des Cipherbuchstabens mit dessen Zahlenwert, den verwendeten Schlüsselbuchstabenwert
        # und den entschlüsselten Buchstaben (Zahl und Buchstabe) in decrypt_list
        decrypt_list.append([value, zeichen, keynumber, decryptnummer, decryptzeichen])

        # keystand auf den nächsten Indexwert setzen und hinzufügen des entschlüsselten Buchstabens in cleartext
        keystand += 1
        keystand = keystand % len(key_list)
        cleartext += decryptzeichen

    return key_list, decrypt_list, cleartext


# ----------------------------------------------------------------------------------------------------------------------
# Kasiski-Test
# ----------------------------------------------------------------------------------------------------------------------
def kasiski(ciphertext: str, ngramm_laenge: int):
    """
    kasiski sucht im übergebenen Text nach allen möglichen ngrammen der Länge ngramm_lange.
    Wird ein n-gramm mindestens dreimal gefunden, wird für dieses anhand der Postitionen der Vorkommen
    der größte gemeinsame Teiler berechnet. Diese n-gramme werden mit deren Positionen und dem größten gemeinsamen
    Teiler in relevante_ng gespeichert und zusammen mit dem hier ebenfalls ermittelten
    am häufigsten vorkommenden größten gemeinsamen Teiler zurückgegeben.

    :param ciphertext: verschlüsselter zu analysierender Text
    :param ngramm_laenge: Zahl, welche die Länge der n-gramme angibt, welche zu finden sind
    :return: relevante_ng (ein Dictionary mit n-grammen, deren Positionen und dem gcd) und h_gcd (der häufigste gcd)
    """

    # Dictionary, welche die n-gramme enthält
    ngramme = {}

    # Iteration über ciphertext.
    # Dabei werden alle vorkommenden n-gramme als key in dem Dictionary n-gramme gespeichert.
    # Als Value zu den gespeicherten n-grammen werden die Abstände zum Textbeginn der jeweiligen Vorkommen gespeichert.
    for text_pos in range(len(ciphertext) - (ngramm_laenge - 1)):
        substring = ciphertext[text_pos: text_pos + ngramm_laenge]

        # wenn betrachteter substring schon vorgekommen ist:
        if substring in ngramme:
            ngramme[substring].append(text_pos)

        # ansonsten wird er neu hinzugefügt
        else:
            ngramme[substring] = [text_pos]

    # Berechnen des größten gemeinsamen Teilers (gcd/ggT) anhand der Abstände zum ersten Vorkommen
    # für alle n-gramme, welche mindestens 3 mal vorkommen.
    # Zudem werden in dem neuen Dictionary relevante_ng alle n-gramme, welche mindestens dreimal vorkommen
    # mit deren Position im Text und dem berechneten gcd gespeichert
    gcds = {}
    relevante_ng = []
    for key, value in ngramme.items():
        if len(value) > 2:

            abstaende = []
            for pos_ngramm in range(len(value) - 1):
                abstaende.append(value[pos_ngramm + 1] - value[0])

            ggt = gcd_berechnung(abstaende)
            relevante_ng.append([key, ngramme[key], ggt])

            # Hinzufügen des berechneten ggT's in das Dictionary gcds
            # für die spätere Ermittlung, welcher gcd am häufigsten vorkommt.
            if ggt in gcds:
                gcds[ggt] = gcds[ggt] + 1
            else:
                gcds[ggt] = 1

    # Ermitteln, welcher gcd am häufigsten vorkommt.
    h_gcd = -1  # enthält den häufigsten gcd
    a_gcd = 0  # enthält die Anzahl wie odt der häufigste gcd vorkommt
    for key, value in gcds.items():
        if value > a_gcd:
            h_gcd = key
            a_gcd = value

    return relevante_ng, h_gcd


# pylint: disable=invalid-name
def gcd_berechnung(abstaende):
    """
    Berechnet den größten gemeinsamen Teiler von zwei oder mehrerer Zahlen
    :param abstaende: Liste mit Zahlen (/Abständen der n-gramm-Postitionenen zum ersten n-gramm)
    :return: der größte gemeinsame Teiler (ggT/gcd)
    """
    r = gcd(abstaende[0], abstaende[1])
    i = 2
    while (r > 1) and (i < len(abstaende)):
        r = gcd(r, abstaende[i])
        i += 1
    return r


# pylint: disable=invalid-name
def gcd(a, b):
    """
    Bekommt zwei Zahlen übergeben für welche der größte gemeinsame Teiler berechnet und zurückgegeben wird.
    :param a: 1. Zahl für welche der größte gemeinsame Teiler berechnet werden soll
    :param b: 2. Zahl für welche der größte gemeinsame Teiler berechnet werden soll
    :return: der größte gemeinsame Teiler von a und b
    """
    while True:
        r = a % b
        a = b
        b = r
        if r == 0:
            break
    return a


# ----------------------------------------------------------------------------------------------------------------------
# Koinzidenzindexmethode
# ----------------------------------------------------------------------------------------------------------------------
def coincidence_index(text):
    """
    Berechnet den Koinzidenzindex des übergebenen Textes
    :param text: zu analysierender verschlüsselter Text
    :return: berechneter Koinzidenzindex als Fließkommazahl
    """

    # Berechnung des Koinzidenzindexes
    c_index = 0
    for i in range(26):
        anzahl = text.count(chr(i + 65))
        c_index = c_index + anzahl * (anzahl - 1)
    c_index = c_index / (len(text) * (len(text) - 1))

    return c_index


def coincidence_test(ciphertext: str, spaltenanzahl: int, schwellwert: float):
    """
    coincidence_test teilt den pbergebenen Text in die gewünschte Anzahl an Spalten auf und berechnet für diese den
    jeweiligen Koincidenzindex. Zudem wird überprüft, ob alle berechneten Koinzidenzindexe über dem übergebenen
    Schwellwert liegen.
    :param ciphertext: der zu analysierende Geheimtext
    :param spaltenanzahl: Anzahl in wie viele Spalten/Texte der Geheimtext aufgeteilt werden soll
    :param schwellwert: der zu berücksichtigende Schwellwert
    :return: die Spaltennzahl, die aufgeteilten Texte, eine Liste mit den Koinzidenzindexen
    und ob diese alle über dem Schwellwert liegen
    """

    # Aufteilen von ciphertext in die gegebene Anzahl von Spalten
    if spaltenanzahl == 1:
        spalten = []
        spalten.append(ciphertext)
    else:
        spalten = textaufteilung(ciphertext, spaltenanzahl)

    # Berechnung der Koinzidenzindexe der entstandenen Texte in Spalten.
    # Da zudem überprüft wird, ob alle berechneten Indexe der Spaltentexte über dem gegebenen Schwellwert liegen,
    # wird result auf False gesetzt, wenn ein Koinzidenzindex kleiner-gleich dem Schwellwert ist.
    c_indexe = []
    for _, value in enumerate(spalten):
        c_indexe.append(coincidence_index(value))

    result = all(map(lambda ci: ci >= schwellwert, c_indexe))

    return len(spalten), spalten, c_indexe, result


def coincidence_berechnung(ciphertext: str, max_spalten: int, schwellwert: float):
    """
    coincidence_berechnung berechnet für alle möglichen Spaltenanzahlen von 1 bis hin zur übergebenen
    max_spalten-Variable für alle daraus entstandenen Spalten/Texte die Koinzidenzindexe, speichert diese und gibt diese
    zurück
    :param ciphertext: verschlüsselter zu analysierender Text
    :param max_spalten: Zahl welche besagt bis zu wie viele Spalten betrachtet werden sollen
    :param schwellwert: Zahl, welche den zu beachtenden Schwellwert angibt
    :return: Liste, welche Listen mit allen Koinzidenzindexen für die jeweiligen Textaufteilungen enthält
    """

    k_indizes = []

    for i in range(max_spalten):
        k_indizes.append(coincidence_test(ciphertext, i + 1, schwellwert))

    return k_indizes


# ----------------------------------------------------------------------------------------------------------------------
# Schlüssselberechnung
# ----------------------------------------------------------------------------------------------------------------------
def mutual_coincidence_index(text_x: str, text_y: str):
    """
    Berechnet den gegenseitigen Koinzidenzindex der zwei übergebenen Texte für jede Verschiebung von text_y.
    Dabei wird der maximale Koinzidenzindex mit dessen Verschiebung ermittelt
    :param text_x: 1. Text für die Berechnung dessen gegenseitigen Koinzidenzindexes
    :param text_y: 2. Text für die Berechnung dessen gegenseitigen Koinzidenzindexes
    :return: alle berechneten gegenseitige Koinzidenzindexe sowie der größte berechnete MIc mit dessen Verschiebung
    """

    mics = []  # Liste mit den berechneten gegenseitigen Koinzidenzindexen und deren verwendeter Verschiebung
    max_mic = -1  # größter berechneter gegenseitiger Koinzidenzindex
    g_maxmic = -1  # die zur Berechnung von max_mic verwendete Verschiebung für text_y

    # Berechnung aller MIc's mit allen um shift_g verschobenen Varianten von text_y
    for shift_g in range(26):

        # Berechnen des gegenseitigen Koinzidenzindexes der beiden gegebenen Texte mit der Verschiebung shift_g
        mic = 0
        for buchstabe in range(26):
            ig = (buchstabe - shift_g) % 26
            mic = mic + text_x.count(chr(buchstabe + 65)) * text_y.count(chr(ig + 65))
        mic = mic / (len(text_x) * len(text_y))

        # Anfügen des berechneten MIc mit der verwendeten Verschiebung shift_g in mics
        mics.append([shift_g, mic])

        # Ermittlung, ob der aktuelle MIc der bisher Maximale ist.
        # Wenn ja, wird dieser mit zugehörigen shift_g gespeichert.
        if mic > max_mic:
            max_mic = mic
            g_maxmic = shift_g

    return mics, max_mic, g_maxmic


# pylint: disable=too-many-locals
def schluesselberechnung(texteingabe, texte, cols: int, schwellwert: float):
    """
    schluesselberechnung berechnet zunächst für alle unterschiedlichen Texktkombinationen den gegenseitigen
    Koinzidenzindex für alle Verschiebungen des zweiten Textes und ermittelt dabei zusätzlich den höchsten Wert.
    All diese Werte werden im 1. Returnwert gespeichert.
    Mithilfe der maximalen gegenseitigen Koinzidenzindexe und deren verwendeten Verschiebung wird eine Matrix zur
    Schlüsselberechnung erstellt und im 2. Returnwert gespeichert.
    Mit dieser Matrix werden alle möglichen Schlüsselvarianten berechnet und jeweils die ersten 42 Zeichen des
    verschlüsselten Textes entschlüsselt

    :param texteingabe: der verschlüsselte von html übermittelte Text
    :param texte: Liste mit aufgeteilten Texten
    :param cols: Spaltenanzahl, welche der Schlüssellänge entspricht
    :param schwellwert: der zu beachtende Schwellwert
    :return: eine Liste, welche für alle ungleichen Textkombinationen alle Koinzidenzindexe mit deren Verschiebung
    enthält, matrix zur Schlüsselberechnung und eine Liste mit 26 Schlüsseln und den damit entschlüsseltem Anfangstext)
    """
    matrix = []
    alle_mcis = []

    # Befüllen der Matrix zur Schlüsselberechnung
    for j in range(cols):
        zeile = []
        gueltiger_key = True
        for i in range(cols):
            # sind i und j identisch kommt an dieser Stelle eine 0 in die Matrix
            if i == j:
                zeile.append(0)
            # sind i und j unterschiedlich werden die gegenseitige Koinzidenzindexe mit allen Verschiebungen berechnet
            else:
                mci = mutual_coincidence_index(texte[i], texte[j])
                # ist der höchste MIc größer gleich wie der gegebene Schwellwert
                # wird die Matrix mit der Verschiebung befüllt
                if mci[1] >= schwellwert:
                    zeile.append(mci[2])
                # ist der MIc kleiner als der Schwellwert wird in die Matrix eine -1 eingetragen
                else:
                    zeile.append(-1)

                    # Aus einer Zeile der Matrix kann nur der Schlüssel ermittelt werden, wenn keine -1 darin vorkommt.
                    # Da dies an dieser Stelle aber der Fall ist, wird gueltiger_key auf False gesetzt.
                    gueltiger_key = False

                alle_mcis.append([i + 1, j + 1, mci[0], mci[1], mci[2]])
        matrix.append([zeile, gueltiger_key, j + 1])

    # Schlüsselberechnung anhand der in matrix enthaltenden Werte
    schluessel = []  # Liste, welche alle 26 möglichen Schlüssel mit dem entschlüsselten Textanfang enthält
    for reihe in range(cols):
        # Wenn die aktuelle Zeile keine -1 enthält und somit der mögliche Schlüssel ermittelbar ist
        if matrix[reihe][1] is True:
            # werden 26 mögliche Schlüssel ermittelt
            keys = []
            for k in range(26):
                key = ""
                for spalte in range(cols):
                    key = key + chr(((k + matrix[reihe][0][spalte]) % 26) + 97)

                # Entschlüsselung des Textanfangs mit erhaltenem Schlüssel
                cleartext = decrypt_tabelle(key, texteingabe[0:42])

                keys.append([chr(k + 97), key, cleartext])
            schluessel.append([reihe + 1, keys])

    return alle_mcis, matrix, schluessel


def textaufteilung(ciphertext: str, spaltenanzahl: int):
    """
    Teilt den übergebenen Text in die ebenfalls übergebene Anzahl an Texten auf.
    :param ciphertext: gegebener ciphertext
    :param spaltenanzahl: Zahl, welche angibt in wie viele Texte text aufgeteilt werden soll
    :return: der in spaltenanzahl aufgeteilte Texte aufgeteilte ciphertext
    """

    # Aufteilen der ersten Buchstaben von ciphertext in die gegebene Anzahl von Spalten
    texte = []
    for i in range(spaltenanzahl):
        texte.append(ciphertext[i])
    aktuelle_spalte = 0

    # Iteration beginnend bei Spaltenanzahl, bei welcher der Rest des Textes in die erzeugten Spalten aufgeteilt wird
    for j in range(spaltenanzahl, len(ciphertext)):
        texte[aktuelle_spalte] = str(texte[aktuelle_spalte] + ciphertext[j])
        aktuelle_spalte += 1
        if aktuelle_spalte > spaltenanzahl - 1:
            aktuelle_spalte = 0
    return texte
