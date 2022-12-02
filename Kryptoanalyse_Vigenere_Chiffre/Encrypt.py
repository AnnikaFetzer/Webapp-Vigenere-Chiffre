
def encrypt_tabelle(key, cleartext):

    encrypt_list = []
    key_list = []
    keystand = 0
    ciphertext = ""

    # umformen von key
    key = key.lower()
    for i in range(len(key)):
        zahl = ord(key[i]) - 97
        if 26 > zahl >= 0:
            key_list.append([key[i], zahl])

    cleartext = cleartext.lower()

    for index in range(len(cleartext)):

        zeichen = ord(cleartext[index]) - 97

        if 26 > zeichen >= 0:

            if keystand >= len(key_list):
                keystand = 0

            keynumber = key_list[keystand][1]
            encryptnummer = (zeichen + keynumber) % 26
            encryptzeichen = chr(encryptnummer + 65)

            encrypt_list.append([cleartext[index], zeichen, keynumber, encryptnummer, encryptzeichen])
            keystand += 1
            ciphertext += encryptzeichen

    # w+: Die Datei erstellen, falls sie nicht existiert, und dann im Schreibmodus öffnen
    file = open('encrypttext.txt', 'w+')
    file.writelines(ciphertext)
    file.close()

    return key_list, encrypt_list, ciphertext