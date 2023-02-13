

function onChangeTextaufteilung(eintragString) {
     let eintrag = JSON.parse(eintragString)
     let spaltenanzahl = eintrag[0]
     let spaltentexte = eintrag[1]
     let koinzidenzindexe = eintrag[2]

    let ausgabe_table = document.getElementById("ci_berechnung")
    let html_code = ""

    // Befüllen der 1. Zeile mit Beschriftungen Spalte, Koinzidenzindex und Text
    html_code = "<tr><th class='mx-auto text-center'>Spalte</th><th class='mx-auto text-center'>Koinzidenzindex</th>"
    html_code += "<th colspan="+ spaltentexte[0].length +">Text</th></tr>"

    for(i=0; i<spaltenanzahl; i++){

        // Einfügen der Spaltennummer und des gerundeten Koinzidenzindexes am Zeilenanfang
        html_code += "<tr><th class='mx-auto text-center'>" + (i+1) + "</th><td>"
        html_code += (Math.round(koinzidenzindexe[i] * 10000)/10000) + "</td>"

        // Einfügen der Buchstaben des Spaltentextes in die Tabelle
        for(j=0; j<spaltentexte[i].length; j++){
            html_code += "<td class='mx-auto text-center'>" + spaltentexte[i][j] + "</td>"
        }

        // Beenden der Zeile
        html_code += "</tr>"
    }

    ausgabe_table.innerHTML = html_code
}