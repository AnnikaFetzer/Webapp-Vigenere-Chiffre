import re
from typing import Union


def textanpassung_upper(text):
    """
    Die Funktion iteriert über den übergebenen Text. Dabei werden alle Zeichen, welche keine Buchstaben von a-z sind
    ignoriert und somit entfernt. Alle erlaubten Buchstaben (die Buchstaben a-z) werden zu einem Großbuchstaben
    transformiert dem String newtext angefügt.
    :param text: anzupassender Text
    :return: angepasster Text
    """
    text = text.upper()
    newtext = ""
    for i in range(len(text)):
        if 65 <= ord(text[i]) <= 90:
            newtext += text[i]

    return newtext


def textanpassung_lower(text):
    """
        Die Funktion iteriert über den übergebenen Text. Dabei werden alle Zeichen, welche keine Buchstaben von a-z sind
        ignoriert und somit entfernt. Alle erlaubten Buchstaben (die Buchstaben a-z) werden zu einem Kleinbuchstaben
        transformiert dem String newtext angefügt.
        :param text: anzupassender Text
        :return: angepasster Text
        """
    text = text.lower()
    newtext = ""
    for i in range(len(text)):
        if 97 <= ord(text[i]) <= 122:
            newtext += text[i]

    return newtext


def zahleneingabe(eingabezahl, kommazahl: bool):
    """
    Überprüft, ob die erfolgte Eingabe einer Zahl entspricht.
    Ist dies der Fall, wird diese anschließend positiv gemacht und zurückgegeben.
    Entspricht die Eingabezahl nicht dem gewünschten Eingabeformat, wird False zurückgegeben.
    :param eingabezahl: auf Eingabeformat zu überprüfender String
    :param kommazahl: gibt an, ob eingabezahl eine Ganzzahl oder Kommazahl sein soll
    :return: die positive Zahl oder bei ungewollem Eingabeformat False
    """
    if kommazahl is True:
        if re.match(r"^-?[0-9]+(\.[0-9]+)?$", eingabezahl) is not None:
            p_zahl = abs(float(eingabezahl))
            return p_zahl
        else:
            return -1
    else:
        if re.match(r"^-?[0-9]+$", eingabezahl):
            p_gzahl = abs(int(eingabezahl))
            return p_gzahl
        else:
            return -1
