

function onClickTextaufteilung(spaltenanzahl, spaltentexte, koinzidenzindexe) {

    let ausgabe_table = document.getElementById("ci_berechnung")
    let zeilenspeicher = ""

    // Befüllen der ersten Zeile mit den Spaltennummern
    zeilenspeicher = "<tr>"
    for(i=1; i <= spaltenanzahl; i++){
        zeilenspeicher += "<th>" + i + "</th>"
    }
    zeilenspeicher += "</tr>"

    // Befüllen der zweiten Spalte mit dem berechneten Koinzidenzindex der Spalte
    zeilenspeicher += "<tr>"
    for(j=0; j < koinzidenzindexe.length; j++){
        zeilenspeicher += "<th>" + koinzidenzindexe[j] + "</th>"
    }
    zeilenspeicher += "</tr>"

    // Befüllen der Spalten mit dem Text
    k = 0
    for(k; k < spaltentexte[spaltenanzahl-1].length; k++){
        zeilenspeicher += "<tr>"
        for(l=0; l < spaltenanzahl; l++){
            zeilenspeicher += "<th>" + spaltentexte[l][k] + "</th>"
        }
        zeilenspeicher += "</tr>"
    }

    ausgabe_table.innerHTML = zeilenspeicher
}