import os

import matplotlib.pyplot as plt
import numpy as np


def create_diagram(text1: str, text2: str, shift: int):
    """
    Berechnet für die übergebenen Texte die Buchstabenhäufigkeiten sowie den gegenseitigen Koinzidenzindex
    und veranschaulicht diese in einem Säulendiagramm.
    :param text1: 1. Text, dessen Buchstabenhäufigkeiten in der Grafik veranschaulicht werden soll
    :param text2: 1. Text, dessen Buchstabenhäufigkeiten in der Grafik veranschaulicht werden soll
    :param shift: Zahl um wie viel text2 verschobe werden soll
    :return: die erzeugte Grafik
    """

    # definieren einer Grafik mit 26 x-Achsenpunkten, welche jeweils eine breite von 0.4 haben
    plt.subplots()
    x_achse_punkte = np.arange(26)
    width = 0.40

    # für jeden Text eine Liste, welche die Häufigkeiten der einzelnen Buchstaben enthält
    frequencies1 = []
    frequencies2 = []

    # Iteration über die 26 Buchstaben.
    # Dabei wird für jeden Text die Häufigkeit des aktuell betrachteten Buchstabens ermittelt
    # und in der jeweiligen Liste gespeichert.
    gki = 0  # der gegenseitige Koinzidenzindex von text1 und text2 mit der Verschiebung um shift
    for i in range(26):
        # shiften von i für Text2
        i_shiftet = (i - shift) % 26

        # Berechnen der Häufigkeit des aktuellen Buchstabens
        frequency1 = text1.count(chr(i + 65)) / len(text1)
        frequency2 = text2.count(chr(i_shiftet + 65)) / len(text2)
        # Anfügen der berechneten Häufigkeit in der Liste
        frequencies1.append(frequency1)
        frequencies2.append(frequency2)

        # Berchnung des gegenseitigen Koinzidenzindexes
        gki += (frequency1 * frequency2)

    # Festlegen der Grafikgröße
    plt.rcParams["figure.figsize"] = (10, 5)

    # Einfügen der berechneten Häufigkeiten der Texte in die Grafik
    plt.bar(x_achse_punkte - 0.2, frequencies1, width, color='steelblue', label="Spalte i")
    plt.bar(x_achse_punkte + 0.2, frequencies2, width, color='lightskyblue',
            label="Spalte j (shift: " + str(shift) + " | MIc: " + str(round(gki, 4)) + ")")

    # Definieren der Punktbeschriftungen der x-Achse sowie der y- und x-Achsenbeschriftung
    plt.xticks(x_achse_punkte,
               ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z'])
    plt.xlabel("chars")
    plt.ylabel("frequency")

    # Einfugen einer Legende
    plt.legend(bbox_to_anchor=(0, 1, 1, 0), loc="lower left")

    # Speichern der Grafik als diagram.png (Wenn vorhanden wird hierbei die alte Grafik überschrieben)
    plt.savefig(os.path.abspath('diagram.png'))

    return os.path.abspath('diagram.png')
