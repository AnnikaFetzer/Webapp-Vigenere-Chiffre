

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
