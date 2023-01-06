
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
}


function bildNeuLaden(texte) {
    let text1_nummer = document.getElementById("text1").selectedIndex
    let text2_nummer = document.getElementById("text2").selectedIndex

    if (text1_nummer == -1 || text2_nummer == -1) {
        // Abbruch, da nichts ausgewählt
        return
    }
    let text1 = texte[text1_nummer][1]
    let text2 = texte[text2_nummer][1]

    let bildUrl = document.getElementById("diagrammbild").src.split("?")[0]
    bildUrl += "?text1=" + text1 + "&text2=" + text2 + "&shift=0"
    document.getElementById("diagrammbild").src = bildUrl
}


function nextBild(){
    let newUrl = document.getElementById("diagrammbild").src.split("&shift=")[0]
    let shift = document.getElementById("diagrammbild").src.split("&shift=")[1]
    shift = parseInt(shift) + 1
    if(shift >= 26){
        shift = 0
    }
    newUrl += "&shift=" + shift
    document.getElementById("diagrammbild").src = newUrl
}


function lastBild(){
    let newUrl = document.getElementById("diagrammbild").src.split("&shift=")[0]
    let shift = document.getElementById("diagrammbild").src.split("&shift=")[1]
    shift = parseInt(shift) - 1
    if(shift < 0){
        shift = 25
    }
    newUrl += "&shift=" + shift
    document.getElementById("diagrammbild").src = newUrl
}