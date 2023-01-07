def encrypt_tabelle(key, cleartext):
    """
    encrypt_tabelle verschlüsselt den übergebenen cleartext mit dem ebenfalls übergebenen Schlüssel.
        Zudem wird für den Schlüssel zur späteren Veranschaulichung in html eine Liste erstellt,
        welche die Schlüsselbuchstaben mit deren zur Entschlüsselung verwendeten Zahlenwert enthält.
        Für denselben Zweck wird auch für die Verschlüsselung eine Liste erstellt. Diese enthält jeweils die
        Cleartextbuchstaben, deren Zahlenwert, die angewandten Schlüsselwerte, die Additionsergebnisse der
        beiden Zahlenwerte sowie die berechneten entschlüsselten Buchstaben
    :param key: der zur Entschlüsselung verwendete Schlüssel
    :param cleartext: der zu verschlüsselnde Text
    :return: key_list (die Schlüsselliste), encrypt_list (dei Verschlüsselungsliste) und der verschlüsselte Text
    """

    """
    :param encrypt_list: Liste für die Veranschaulichung der Verschlüsselung
    :param key_list: Liste für die Veranschaulichung des Schlüssels
    :param keystand: speichert einen Index von key 
    :param ciphertext: enthält den verschlüsselten Text
    """
    encrypt_list = []
    key_list = []
    keystand = 0
    ciphertext = ""

    # Entfernen ungewollter Zeichen in key und vereinheitlichen der Groß- und Kleinschreibung
    key = textanpassung_lower(key)
    # Iteration über die Schlüssellänge. Dabei werden die Buchstaben des Schlüssels mit deren
    # zur Entschlüsselung benötigten und hier berechneten Zahlenwert der Liste key_list hinzugefügt
    for i in range(len(key)):
        zahl = ord(key[i]) - 97
        key_list.append([key[i], zahl])

    # Sicherstellung, dass ciphertext den gewollten Anforderungen entspricht
    # d.h. nur die die 26 Standardbuchstaben, welche nach textanpassung alle Großbuchstaben sind
    cleartext = textanpassung_lower(cleartext)

    # Iteration über die Cleartextindexe
    for index in range(len(cleartext)):

        # Umwandlung des Buchstabens in eine Zahl
        zeichen = ord(cleartext[index]) - 97

        """
        Hier wird das betrachtete Zeichen des Klartextet mit dem Schlüsselzeichenwert, welcher sich in dem gespeicherten
        Indexwert in key befindet, durch Addition der beiden Buchstabenwerte berechnet. Zudem werden der verwendetet
        Schlüsselzeichenwert, der Klartextbuchstabe (als Zichen und Zahl) und der verschlüsselte Buchstabe
        (ebenfalls als Zeichen und Zahl) in der Verschlüsselungsliste encrypt_list hinzugefügt
        """
        keynumber = key_list[keystand][1]
        encryptnummer = (zeichen + keynumber) % 26
        encryptzeichen = chr(encryptnummer + 65)
        encrypt_list.append([cleartext[index], zeichen, keynumber, encryptnummer, encryptzeichen])

        # keystand auf den nächsten Indexwert setzen und hinzufügen des verschlüsselten Buchstabens in ciphertext
        keystand += 1
        keystand = keystand % len(key_list)
        ciphertext += encryptzeichen

    # todo: anders lösen
    # w+: Die Datei erstellen, falls sie nicht existiert, und dann im Schreibmodus öffnen
    file = open('encrypttext.txt', 'w+')
    file.writelines(ciphertext)
    file.close()

    return key_list, encrypt_list, ciphertext


def decrypt_tabelle(key, ciphertext):
    """
    decrypt_tabelle entschlüsselt den übergebenen ciphertext mit dem ebenfalls übergebenen Schlüssel.
    Zudem wird für den Schlüssel zur späteren Veranschaulichung in html eine Liste erstellt,
    welche die Schlüsselbuchstaben mit deren zur Entschlüsselung verwendeten Zahlenwert enthält.
    Für denselben Zweck wird auch für die Entschlüsselung eine Liste erstellt. Diese enthält jeweils die
    Ciphertextbuchstaben, deren Zahlenwert, der angewante Schlüsselwert, das Subtraktionsergebnis der beiden Zahlenwerte
    sowie den berechneten entschlüsselten Buchstaben
    :param key: der zur Entschlüsselung verwendete Schlüssel
    :param ciphertext: der zu entschlüsselnde Text
    :return: key_list, decrypt_list, cleartext
    """

    '''
    :param decrypt_list: Liste für die Veranschaulichung der Entschlüsselung
    :param key_list: Liste für die Veranschaulichung des Schlüssels
    :param keystand: speichert einen Index von key 
    :param cleartext: enthält den entschlüsselten Text
    '''
    decrypt_list = []
    key_list = []
    keystand = 0
    cleartext = ""

    # Entfernen ungewollter Zeichen in key und vereinheitlichen der Groß- und Kleinschreibung
    key = textanpassung_lower(key)
    # Iteration über die Schlüssellänge. Dabei werden die Buchstaben des Schlüssels mit deren
    # zur Entschlüsselung benötigten und hier berechneten Zahlenwert der Liste key_list hinzugefügt
    for i in range(len(key)):
        zahl = ord(key[i]) - 97
        key_list.append([key[i], zahl])

    # Sicherstellung, dass ciphertext den gewollten Anforderungen entspricht
    # d.h. nur die die 26 Standardbuchstaben, welche nach textanpassung alle Großbuchstaben sind
    ciphertext = textanpassung_upper(ciphertext)

    # Iteration über den bereinigten ciphertext
    for index in range(len(ciphertext)):

        # Umwandlung des betrachteten Buchstabens in eine Zahl (zwischen 0 und 25)
        zeichen = ord(ciphertext[index]) - 65

        # enthält den zur Entschlüsselung nötigen Schlüsselbuchstabenwert
        keynumber = key_list[keystand][1]

        # Berechnung des Wertes, des entschlüsselten Buchstabens
        decryptnummer = (zeichen - keynumber) % 26

        # Umwandlung des entschlüsselten Buchstabenwertes in den entschlüsselten Buchstaben
        decryptzeichen = chr(decryptnummer + 97)

        # Hinzufügen des Cipherbuchstabens mit dessen Zahlenwert, den verwendeten Schlüsselbuchstabenwert
        # und den entschlüsselten Buchstaben (Zahl und Buchstabe) in decrypt_list
        decrypt_list.append([ciphertext[index], zeichen, keynumber, decryptnummer, decryptzeichen])

        # keystand auf den nächsten Indexwert setzen und hinzufügen des entschlüsselten Buchstabens in cleartext
        keystand += 1
        keystand = keystand % len(key_list)
        cleartext += decryptzeichen

    # todo: besser lösen
    # w+: Die Datei erstellen, falls sie nicht existiert, und dann im Schreibmodus öffnen
    # dabei wird der entschlüsselte Text in die Datei geschrieben und die Datei im Anschluss geschlossen
    file = open('decrypttext.txt', 'w+')
    file.writelines(cleartext)
    file.close()

    return key_list, decrypt_list, cleartext


def kasiski(ciphertext: str, ngramm_laenge: int):

    # Sicherstellung, dass mit ciphertext den gewollten Anforderungen entspricht
    # d.h. nur die die 26 Standardbuchstaben, welche nach textanpassung alle Großbuchstaben sind
    ciphertext = textanpassung_upper(ciphertext)

    # Dictionary, welche die n-gramme enthält
    ngramme = dict()

    """
    Iteration über ciphertext.
    Dabei werden alle vorkommenden n-gramme als key in dem Dictionary n-gramme gespeichert.
    Als Value zu den gespeicherten n-grammen werden die Abstände zum Textbeginn der jeweiligen Vorkommen gespeichert.
    """
    for n in range(len(ciphertext)-(ngramm_laenge - 1)):

        substring = ciphertext[n: n + ngramm_laenge]

        # wenn betrachteter substring schon vorgekommen ist:
        if substring in ngramme.keys():
            ngramme[substring].append(n)

        # ansonsten wird er neu hinzugefügt
        else:
            ngramme[substring] = [n]

    """
    Berechnen des größten gemeinsamen Teilers (gcd/ggT) anhand der Abstände zum ersten Vorkommen 
    für alle n-gramme, welche mindestens 3 mal vorkommen.
    Zudem werden in dem neuen Dictionary relevante_ng alle n-gramme, welche mindestens dreimal vorkommen
    mit deren Position im Text und dem berechneten gcd gespeichert
    """
    gcds = dict()
    relevante_ng = []
    for key, value in ngramme.items():
        if len(value) > 2:

            abstaende = []
            for m in range(len(value) - 1):
                abstaende.append(value[m+1] - value[0])

            ggt = gcd_berechnung(abstaende)
            relevante_ng.append([key, ngramme[key], ggt])

            """
            Hinzufügen des berechneten ggT's in das Dictionary gcds 
            für die spätere Ermittlung, welcher gcd am häufigsten vorkommt.
            """
            if ggt in gcds.keys():
                gcds[ggt] = gcds[ggt] + 1
            else:
                gcds[ggt] = 1

    """
    Ermitteln, welcher gcd am häufigsten vorkommt.
    """
    h_gcd = -1   # enthält den häufigsten gcd
    a_gcd = 0   # enthält die Anzahl wie odt der häufigste gcd vorkommt
    for key in gcds:
        if gcds[key] > a_gcd:
            h_gcd = key
            a_gcd = gcds[key]

    return relevante_ng, h_gcd


def textanpassung_upper(ciphertext):
    ciphertext = ciphertext.upper()
    n_ct = ""
    for i in range(len(ciphertext)):
        if 65 <= ord(ciphertext[i]) <= 90:
            n_ct += ciphertext[i]

    return n_ct


def textanpassung_lower(text):
    text = text.lower()
    n_ct = ""
    for i in range(len(text)):
        if 97 <= ord(text[i]) <= 122:
            n_ct += text[i]

    return n_ct


def gcd_berechnung(abstaende):
    r = gcd(abstaende[0], abstaende[1])
    i = 2
    while (r > 1) and (i < len(abstaende)):
        r = gcd(r, abstaende[i])
        i += 1
    return r


def gcd(a, b):
    while True:
        r = a % b
        a = b
        b = r
        if r == 0:
            break
    return a


def coincidence_index(text):
    """
    Berechnet den Koinzidenzindex des übergebenen Textes
    :param text: zu analysierender verschlüsselter Text
    :return: berechneter Koinzidenzindex als Fließkommazahl
    """

    # Sicherstellung, dass mit ciphertext den gewollten Anforderungen entspricht
    # d.h. nur die die 26 Standardbuchstaben großgeschrieben
    text = textanpassung_upper(text)

    # Berechnung des Koinzidenzindexes
    c_index = 0
    for i in range(26):
        anzahl = text.count(chr(i + 65))
        c_index = c_index + anzahl * (anzahl-1)
    c_index = c_index / (len(text) * (len(text) - 1))

    return c_index


def coincidence_test(ciphertext: str, spaltenanzahl: int, schwellwert: float):
    """
    :param ciphertext:
    :param spaltenanzahl:
    :param schwellwert:
    :return:
    """

    # Aufteilen von ciphertext in die gegebene Anzahl von Spalten
    spalten = []
    if spaltenanzahl > 1:
        for i in range(spaltenanzahl):
            spalten.append(ciphertext[i])
        s = 0
        for j in range(spaltenanzahl, len(ciphertext)):
            spalten[s] = str(spalten[s] + ciphertext[j])
            s += 1
            if s > spaltenanzahl - 1:
                s = 0
    # wenn nur eine Spalte gegeben ist vereinfachte Lösung, da kein Aufteilen von ciphertext nötig ist.
    else:
        spalten.append(ciphertext)

    """
    Berechnung der Koinzidenzindexe der entstandenen Texte in spalten.
    Da zudem überprüft wird, ob alle berechneten Indexe der Spaltentexte über dem gegebenen Schwellwert liegen,
    wird result auf False gesetzt wenn ein Koinzidenzindex kleiner-gleich dem Schwellwert ist.
    """
    c_indexe = []
    result = True
    for k in range(len(spalten)):
        c_indexe.append(coincidence_index(spalten[k]))
        if c_indexe[k] <= schwellwert:
            result = False

    return len(spalten), spalten, c_indexe, result


def coincidence_berechnung(ciphertext: str, max_spalten: int, schwellwert: float):
    """
    :param ciphertext:
    :param max_spalten:
    :param schwellwert:
    :return:
    """
    # Sicherstellung, dass mit ciphertext den gewollten Anforderungen entspricht
    # d.h. nur die die 26 Standardbuchstaben großgeschrieben
    ciphertext = textanpassung_upper(ciphertext)

    k_indizes = []

    for i in range(max_spalten):
        k_indizes.append(coincidence_test(ciphertext, i+1, schwellwert))

    return k_indizes


# def mutual_coincidence_index(ciphertext: str, cols: int, col_i: int, col_j: int, threshold: float):
def mutual_coincidence_index(text_x: str, text_y: str):
    """
    Berechnet den gegenseitigen Koinzidenzindex der zwei übergebenen Texte für jede Verschiebung von text_y.
    Dabei wird der maximale Koinzidenzindex mit dessen Verschiebung ermittelt
    :param text_x:
    :param text_y:
    :return: alle berechneten gegenseitige Koinzidenzindexe sowie der größte berechnete MIc mit dessen Verschiebung
    """

    mics = []
    max_mic = -1
    g_maxmic = -1

    # Berechnung aller MIc's mit allen um g verschobenen Varianten von text_y
    for g in range(26):

        # Berechnen des gegenseitigen Koinzidenzindexes der beiden gegebenen Texte mit der Verschiebung g
        mic = 0
        for i in range(26):
            ig = (i - g) % 26
            mic = mic + text_x.count(chr(i + 65)) * text_y.count(chr(ig + 65))
        mic = mic / (len(text_x) * len(text_y))

        # anfügen des berechneten MIc mit der verwendeten Verschiebung g in mics
        mics.append([g, mic])

        # Ermittlung, ob der aktuelle MIc der bisher Maximale ist.
        # Wenn ja, wird dieser mit zugehörigen g gespeichert.
        if mic > max_mic:
            max_mic = mic
            g_maxmic = g

    return mics, max_mic, g_maxmic


def schluesselberechnung(texteingabe, texte, cols: int, schwellwert: float):
    """
    :param texteingabe:
    :param texte:
    :param cols:
    :param schwellwert:
    :return:
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
                """
                ist der höchste MIc größer gleich wie der gegebene Schwellwert 
                wird die Matrix mit der Verschiebung befüllt
                """
                if mci[1] >= schwellwert:
                    zeile.append(mci[2])
                # ist der MIc kleiner als der Schwellwert wird in die Matrix eine -1 eingetragen
                else:
                    zeile.append(-1)
                    """ 
                    Aus einer Zeile der Matrix kann nur der Schlüssel ermittelt werden wenn keine -1 darin vorkommt.
                    Da dies an dieser Stelle aber der Fall ist, wird gueltiger_key auf False gesetzt.
                    """
                    gueltiger_key = False

                alle_mcis.append([i+1, j+1, mci[0], mci[1], mci[2]])
        matrix.append([zeile, gueltiger_key, j+1])

    # Schlüsselberechnung
    schluessel = []
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
                cleartext = decrypt_tabelle(key, texteingabe[0:24])

                keys.append([chr(k + 97), key, cleartext])
            schluessel.append([reihe+1, keys])

    return alle_mcis, matrix, schluessel


def textaufteilung(ciphertext: str, spaltenanzahl: int):
    """
    :param ciphertext: gegebener ciphertext
    :param spaltenanzahl: Zahl, welche angibt in wie viele Texte text aufgeteilt werden soll
    :return: der in spaltenanzahl aufgeteilte Texte aufgeteilte ciphertext
    """

    # Sicherstellung, dass der gegebene Text den gewollten Anforderungen entspricht
    # d.h. nur die die 26 Standardbuchstaben
    ciphertext = textanpassung_upper(ciphertext)

    # Aufteilen von ciphertext in die gegebene Anzahl von Spalten
    texte = []
    for i in range(spaltenanzahl):
        texte.append(ciphertext[i])
    aktuelle_spalte = 0

    # Iteration beginnend bei Spaltenanzahl
    for j in range(spaltenanzahl, len(ciphertext)):
        texte[aktuelle_spalte] = str(texte[aktuelle_spalte] + ciphertext[j])
        aktuelle_spalte += 1
        if aktuelle_spalte > spaltenanzahl - 1:
            aktuelle_spalte = 0
    return texte
