

function onClickTextaufteilung(spaltenanzahl, spaltentexte, koinzidenzindexe) {

    let ausgabe_table = document.getElementById("ci_berechnung")
    let zeilenspeicher = ""

    // Befüllen der ersten Zeile mit den Spaltennummern
    zeilenspeicher = "<tr>"
    for(i=1; i <= spaltenanzahl; i++){
        zeilenspeicher += "<td>" + i + "</td>"
    }
    zeilenspeicher += "</tr>"

    // Befüllen der zweiten Spalte mit dem berechneten Koinzidenzindex der Spalte
    zeilenspeicher += "<tr>"
    for(j=0; j < koinzidenzindexe.length; j++){
        zeilenspeicher += "<td>" + koinzidenzindexe[j] + "</td>"
    }
    zeilenspeicher += "</tr>"

    // Befüllen der Spalten mit dem Text
    k = 0
    for(k; k < spaltentexte[spaltenanzahl-1].length; k++){
        zeilenspeicher += "<tr>"
        for(l=0; l < spaltenanzahl; l++){
            zeilenspeicher += "<td>" + spaltentexte[l][k] + "</td>"
        }
        zeilenspeicher += "</tr>"
    }

    ausgabe_table.innerHTML = zeilenspeicher
}