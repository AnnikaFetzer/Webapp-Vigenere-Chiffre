
function onClickSchluessel(k, schluessel){

    let ausgabe_table = document.getElementById("schluessel_berechnung")

    htmlCode = "<tr><th>k" + k + "</th>" + "<th>Schlüssel</th>" + "<th>Anfangstück des Klartexts</th></tr>"


    //Zeilenposition von k in schluessel finden
    index = -1
    for(m=0; m<schluessel.length; m++){
        if(schluessel[m][0]==k){
            index = m
        }
    }

    // Tabelleneinträge erzeugen
    for(n=0;n<26;n++){
        htmlCode += "<tr><td>" + schluessel[index][1][n][0] + "</td>"
        htmlCode += "<td>" + schluessel[index][1][n][1] + "</td>"
        htmlCode += "<td>" + schluessel[index][1][n][2] + "..." + "</td></tr>"
    }
    ausgabe_table.innerHTML = htmlCode







/*
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
    */

}