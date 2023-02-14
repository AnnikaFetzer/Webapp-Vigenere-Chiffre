
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

def zahleneingabe(eingabezahl, kommazahl: bool):
    komma = False