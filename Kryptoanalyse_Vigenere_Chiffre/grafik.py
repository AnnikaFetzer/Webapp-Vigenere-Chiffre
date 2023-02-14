import matplotlib.pyplot as plt
import numpy as np


def create_diagram(text1: str, text2: str, shift: int):
    fig, ax = plt.subplots()

    x = np.arange(26)

    width = 0.40

    # für jeden Text eine Liste, welche die Häufigkeiten der einzelnen Buchstaben enthält
    frequencies1 = []
    frequencies2 = []

    '''
    Iteration über die 26 Buchstaben. 
    Dabei wird für jeden Text die Häufigkeit des aktuell betrachteten Buchstabens ermittelt
    und in der jeweiligen Liste gespeichert.
    '''
    gki = 0
    for i in range(26):
        # shiften von i für Text2
        iShiftet = (i - shift) % 26

        # Berechnen der Häufigkeit des aktuellen Buchstabens
        frequency1 = text1.count(chr(i + 65)) / len(text1)
        frequency2 = text2.count(chr(iShiftet + 65)) / len(text2)
        # Anfügen der berechneten Häufigkeit in der Liste
        frequencies1.append(frequency1)
        frequencies2.append(frequency2)

        gki += (frequency1 * frequency2)
    # gki = gki / (len(text1) * len(text2))

    plt.rcParams["figure.figsize"] = (10, 5)

    # plt.bar(x - 0.2, frequencies1, width, color='steelblue')
    # plt.bar(x + 0.2, frequencies2, width, color='lightskyblue')
    plt.bar(x - 0.2, frequencies1, width, color='steelblue', label="Spalte i")
    plt.bar(x + 0.2, frequencies2, width, color='lightskyblue',
            label="Spalte j (shift: " + str(shift) + " | MIc: " + str(round(gki, 4)) + ")")

    plt.xticks(x,
               ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z'])
    plt.xlabel("chars")

    plt.ylabel("frequency")

    # plt.legend(["Spalte i", "Spalte j (shift: " + str(shift) + ")"])
    plt.legend(bbox_to_anchor=(0, 1, 1, 0), loc="lower left")

    plt.savefig('diagram.png')

    return 'diagram.png'
