
function onClickSchluessel(eintragString){
    let eintrag = JSON.parse(eintragString)
    let schluessel = eintrag['schluessel']
    let k = eintrag['k']

    // die in html enthalte Element mit der id schluessel_berechnung wird in ausgabe_table gespeichert
    let ausgabe_table = document.getElementById("schluessel_berechnung")

    // in den String htmlCode wird der für die Ausgabe der ersten Tabellenzeile benötigte html-Code gespeichert
    htmlCode = "<tr><th>k" + k + "</th>" + "<th>Schlüssel</th>" + "<th>Anfangstück des Klartexts</th></tr>"

    //Zeilenposition von k in schluessel finden und in index speichern
    index = -1
    for(m=0; m<schluessel.length; m++){
        if(schluessel[m][0]==k){
            index = m
        }
    }

    // hmtl_code für die 26 Tabelleneinträge (genutzer Buchstabe, entstandener Schlüssel, entschlüsselter Textanfang)
    // erzeugen und dem String htmlcode anfügen
    for(n=0;n<26;n++){
        htmlCode += "<tr><td>" + schluessel[index][1][n][0] + "</td>"
        htmlCode += "<td>" + schluessel[index][1][n][1] + "</td>"
        htmlCode += "<td>" + schluessel[index][1][n][2] + "..." + "</td></tr>"
    }

    // erzeugter html-Code in htmlCode an das Element zurückgeben
    ausgabe_table.innerHTML = htmlCode
}


function bildNeuLaden(texte) {
    // die Elemente zu den ids text1 und text2 in text1_nummer und text2_nummer speichern
    let text1_nummer = document.getElementById("text1").selectedIndex
    let text2_nummer = document.getElementById("text2").selectedIndex

    // Wenn eines oder beides der Elemente -1 enthält Abbruch, da dort nichts ausgewählt ist
    if (text1_nummer == -1 || text2_nummer == -1) {
        return
    }

    //speichern des jeweils ausgwählten Textes/der ausgewählten Spalte in text1 und text2
    let text1 = texte[text1_nummer][1]
    let text2 = texte[text2_nummer][1]

    //einfügen von text1 und text2 in die Url der Grafik
    let bildUrl = document.getElementById("diagrammbild").src.split("?")[0]
    bildUrl += "?text1=" + text1 + "&text2=" + text2 + "&shift=0"
    document.getElementById("diagrammbild").src = bildUrl
}


function nextBild(){
    // speichern des Anfangs der Url der Grafik in newUrl
    let newUrl = document.getElementById("diagrammbild").src.split("&shift=")[0]
    // speichern des shiftwertes der Url der Grafik in shift
    let shift = document.getElementById("diagrammbild").src.split("&shift=")[1]

    // erhöhen des Shiftwertes um 1, um diesen dann in der Url zu ersetzen
    shift = (parseInt(shift) + 1) %26
    newUrl += "&shift=" + shift
    document.getElementById("diagrammbild").src = newUrl
}


function lastBild(){
    // speichern des Anfangs der Url der Grafik in newUrl
    let newUrl = document.getElementById("diagrammbild").src.split("&shift=")[0]
    // speichern des shiftwertes der Url der Grafik in shift
    let shift = document.getElementById("diagrammbild").src.split("&shift=")[1]

    // Shiftwert um 1 reduzieren und diesen in der Url zu ersetzen
    shift = parseInt(shift) - 1
    if(shift < 0){
        shift = 25
    }
    newUrl += "&shift=" + shift
    document.getElementById("diagrammbild").src = newUrl
}