import re


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

    for _, value in enumerate(text):
        if 65 <= ord(value) <= 90:
            newtext += value

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

    for _, value in enumerate(text):
        if 97 <= ord(value) <= 122:
            newtext += value

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
        return -1

    if re.match(r"^-?[0-9]+$", eingabezahl):
        p_gzahl = abs(int(eingabezahl))
        return p_gzahl
    return -1
