
import matplotlib.pyplot as plt
import numpy as np


def create_diagram(text1: str, text2: str, shift: int):

    fig, ax = plt.subplots()

    x = np.arange(26)

    # y1 = [34, 56, 12, 89, 67, 34, 56, 12, 89, 67, 34, 56, 12, 89, 67, 34, 56, 12, 89, 67, 34, 56, 12, 89, 67, 8]
    # y2 = [12, 56, 78, 45, 90, 12, 56, 78, 45, 90, 12, 56, 78, 45, 90, 12, 56, 78, 45, 90, 12, 56, 78, 45, 90, 8]

    width = 0.40

    # y1 = buchstabenhaeufigkeit(text1)
    # y2 = buchstabenhaeufigkeit(text2)


    # für jeden Text eine Liste, welche die Häufigkeiten der einzelnen Buchstaben enthält
    frequencies1 = []
    frequencies2 = []

    '''
    Iteration über die 26 Buchstaben. 
    Dabei wird für jeden Text die Häufigkeit des aktuell betrachteten Buchsabens ermittelt
    und in der jeweiligen Liste gespeichert.
    '''
    for i in range(26):
        # shiften von i für Text2
        iShiftet = (i-shift) % 26

        # Berechnen der Häufigkeit des aktuelen Buchstabens
        frequency1 = text1.count(chr(i + 65)) / len(text1)
        frequency2 = text2.count(chr(iShiftet + 65)) / len(text2)
        # Anfügen der berechneten Häufigkeit in der Liste
        frequencies1.append(frequency1)
        frequencies2.append(frequency2)


    plt.bar(x - 0.2, frequencies1, width, color='orange')
    plt.bar(x + 0.2, frequencies2, width, color='green')

    plt.xticks(x,
               ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z'])
    plt.xlabel("chars")

    plt.ylabel("frequency")

    plt.legend(["Spalte i", "Spalte j"])

    plt.savefig('diagram.png')

    return 'diagram.png'





