import numpy as np


def encrypt_tabelle(key, cleartext):

    encrypt_list = []
    key_list = []
    keystand = 0
    ciphertext = ""

    #umformen von key
    for i in range(len(key)):
        zahl = ord(key[i]) - 97
        if zahl < 26 and zahl >= 0:
            key_list.append([key[i], zahl])


    cleartext = cleartext.lower()

    for index in range(len(cleartext)):

        zeichen =ord(cleartext[index])-97

        if zeichen < 26 and zeichen >= 0:

            if keystand >= len(key):
                keystand = 0

            keynumber = key_list[keystand][1]
            encryptnummer = (zeichen + keynumber) % 26
            encryptzeichen = chr(encryptnummer + 97)

            encrypt_list.append([cleartext[index], zeichen, keynumber, encryptnummer, encryptzeichen])
            keystand += 1
            ciphertext += encryptzeichen



    file = open('encrypttext.txt', 'w+')    #w+: Die Datei erstellen, falls sie nicht existiert, und dann im Schreibmodus öffnen
    file.writelines(ciphertext)
    file.close()

    return key_list, encrypt_list, ciphertext

