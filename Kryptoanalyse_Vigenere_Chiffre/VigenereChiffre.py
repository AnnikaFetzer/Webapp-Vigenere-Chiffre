

def decrypt_tabelle(key, ciphertext):

    decrypt_list = []
    key_list = []
    keystand = 0
    cleartext = ""

    # Umformen von key
    key = key.lower()
    for i in range(len(key)):
        zahl = ord(key[i]) - 97
        if 26 > zahl >= 0:
            key_list.append([key[i], zahl])

    for index in range(len(ciphertext)):

        zeichen = ord(ciphertext[index]) - 65

        if 26 > zeichen >= 0:

            if keystand >= len(key_list):
                keystand = 0

            keynumber = key_list[keystand][1]
            decryptnummer = (zeichen - keynumber) % 26
            decryptzeichen = chr(decryptnummer + 97)

            decrypt_list.append([ciphertext[index], zeichen, keynumber, decryptnummer, decryptzeichen])
            keystand += 1
            cleartext += decryptzeichen

    # w+: Die Datei erstellen, falls sie nicht existiert, und dann im Schreibmodus öffnen
    # dabei wird der entschlüsselte Text in die Datei geschrieben und die Datei im Anschluss geschlossen
    file = open('decrypttext.txt', 'w+')
    file.writelines(cleartext)
    file.close()

    return key_list, decrypt_list, cleartext


def kasiski(ciphertext: str, ngramm_laenge: int):

    # Sicherstellung, dass mit ciphertext den gewollten Anforderungen entspricht
    # d.h. nur die die 26 Standardbuchstaben großgeschrieben
    ciphertext = textanpassung(ciphertext)

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


def textanpassung(ciphertext):
    # todo ciphertext (in String mit Großbuchstaben) konvertieren
    # todo: zudem Fehler ausschließen

    ciphertext.upper()
    n_ct = ""
    for i in range(len(ciphertext)):
        if 65 <= ord(ciphertext[i]) <= 90:
            n_ct += ciphertext[i]

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
    text = textanpassung(text)

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
    ciphertext = textanpassung(ciphertext)

    k_indizes = []

    for i in range(max_spalten):
        k_indizes.append(coincidence_test(ciphertext, i+1, schwellwert))

    return k_indizes


# def mutual_coincidence_index(ciphertext: str, cols: int, col_i: int, col_j: int, threshold: float):
def mutual_coincidence_index(text_x: str, text_y: str):
    mic = 0
    for i in range(26):
        mic = mic + text_x.count(chr(i+65)) * text_y.count(chr(i+65))
    mic = mic / (len(text_x) * len(text_y))

    return mic


def max_mci(text_x: str, text_y: str):

    # todo: mci
    #  - Spalten/Texte befüllen (text_x und text_y)
    #  - ermitteln welcher mci mit Verschiebung der Maximale ist + ermittlung aller mcis mit verschiebung
    #  - Tabelle befüllen, x/i == y/j  -> 0 || mci < schwellwert -> -1
    return








