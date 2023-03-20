
function onChangeNgramm(eintragString) {
    // Elemente aus html holen und speichern
    let text = document.getElementById('cipher_text').value
    let ausgabe_text = document.getElementById('ausgabe_text_farbig')
    let ausgabe_pos = document.getElementById('ausgabe_positionen')

    if (eintragString == "") {
        ausgabe_text.innerHTML = htmlCode = ""
        ausgabe_pos.innerHTML = htmlCode = ""
        return
    }

    let eintrag = JSON.parse(eintragString)
    let ngram = eintrag[0]
    let idxs = eintrag[1]
    let gcd = eintrag[2]

    let ausgabe_text_html = ''
    let ausgabe_positionen_html = ''

    //Ausgabe der Positionen des ausgewählten n-gramms
    ausgabe_positionen_html = '<b class="text-primary">' + ngram + "</b> kommt an diesen Positionen vor:" + '<br>'

    // Anfang Grid Layout
    ausgabe_positionen_html += '<div style="display: grid; grid-template-columns: repeat(auto-fill, 120px)">'

    for (j=0; j<idxs.length; j++){
         ausgabe_positionen_html += "<div>i" + j + " = " + idxs[j] + "</div>"
    }

    // Ende Grid Layout
    ausgabe_positionen_html += '</div>'

    // Ausgabe gcd
    ausgabe_positionen_html += '<br><br>gcd von <b class="text-primary">' + ngram + '</b>:  <b>' + gcd + '</b>'

    // Zusammengebauten html String dem Objekt in der Seite zuweisen
    ausgabe_pos.innerHTML = ausgabe_positionen_html

    /*
     Ausgabe des eingegebenen verschlüsselten Textes,
     in welchen die Vorkommen des ausgewählten n-gramms eingefärbt sind.
    */
    if(idxs[0] != 0){
        ausgabe_text_html += text.substring(0, idxs[0])
    }
    for (i=0; i<idxs.length; i++){
        let a = '<b class="text-primary">'
        let b = text.substring(idxs[i], idxs[i]+ngram.length)
        let c = '</b>'
        let d = ''
        if (i+1 != idxs.length) {
            d = text.substring(idxs[i]+ngram.length, idxs[i+1])
        }
        else {
            d = `${text.substring(idxs[i]+ngram.length)}<br><br>`
        }
        ausgabe_text_html +=  a + b  + c
        ausgabe_text_html += d
    }

    // Zusammengebauten html String dem Objekt in der Seite zuweisen
    ausgabe_text.innerHTML = ausgabe_text_html
}