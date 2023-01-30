

function onChangeTextaufteilung(eintragString) {
     let eintrag = JSON.parse(eintragString)
     let spaltenanzahl = eintrag[0]
     let spaltentexte = eintrag[1]
     let koinzidenzindexe = eintrag[2]

    let ausgabe_table_head = document.getElementById("ci_berechnung_head")
    let ausgabe_table_body = document.getElementById("ci_berechnung_body")
    let zeilenspeicher_head = ""
    let zeilenspeicher_body = ""

    // Befüllen der ersten Zeile mit den Spaltennummern
    zeilenspeicher_head = "<tr>"
    zeilenspeicher_head += '<th>Spalte</th>'

    for(i=1; i <= spaltenanzahl; i++){
        zeilenspeicher_head += '<th>' + i + '</th>'
    }
    zeilenspeicher_head += "</tr>"

    // Befüllen der zweiten Zeile mit dem berechneten Koinzidenzindex der Spalte
    zeilenspeicher_body += "<tr>"
    zeilenspeicher_body += '<th>Koinzidenzindex</td>'

    for(j=0; j < koinzidenzindexe.length; j++){
        zeilenspeicher_body += "<td>" + koinzidenzindexe[j] + "</td>"
    }
    zeilenspeicher_body += "</tr>"

    // Befüllen der Spalten mit dem Text
    k = 0
    for(k; k < spaltentexte[spaltenanzahl-1].length; k++){
        zeilenspeicher_body += "<tr>"
        if (k == 0) {

        zeilenspeicher_body += '<td rowspan="' + spaltentexte[spaltenanzahl-1].length + '"></td>'
        }

        for(l=0; l < spaltenanzahl; l++){
            zeilenspeicher_body += "<td>" + spaltentexte[l][k] + "</td>"
        }
        zeilenspeicher_body += "</tr>"
    }

    ausgabe_table_head.innerHTML = zeilenspeicher_head
    ausgabe_table_body.innerHTML = zeilenspeicher_body
}