

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


def kasiski(ciphertext, ngramm_laenge):

    # Sicherstellung, dass mit ciphertext den gewollten Anforderungen entspricht
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
            relevante_ng = ([key, ngramme[key], ggt])

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

    return ciphertext


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
        if r is 0:
            break
    return a

# def koinzidenzindex(ciphertext, spalten, threschold):

    # for i in range(26):
#
    # k_index = 0
    # return k_index
