
function onClickNgramm(ngram, idxs, gcd) {
    // Ich bin ein Kommentar
    let text = document.getElementById('cipher_text').value
    // let vorkommen = document.getElementById('ngramme').value

    let ausgabe_text = document.getElementById('ausgabe_text_farbig')
    let ausgabe_pos = document.getElementById('ausgabe_positionen')

    /*
    Ausgabe der Positionen des ausgewählten n-gramms
    */
    ausgabe_pos.innerHTML = '<br><br>' + ngram + " kommt an diesen Positionen vor:" + '<br>'
    for (j=0; j<idxs.length; j++){
         ausgabe_pos.innerHTML += "i" + j + " = " + idxs[j]
         if(j+1 < idxs.length){
             ausgabe_pos.innerHTML += ",  "
         }
    }

    // Ausgabe gcd
    ausgabe_pos.innerHTML += "<br><br>" + "gcd von " + ngram + ":  " + gcd

    ausgabe_text.innerHTML = '<br><br>'

    /*
     Ausgabe des eingegebenen verschlüsselten Textes,
     in welchen die Vorkommen des ausgewählten n-gramms eingefärbt sind.
    */
    if(idxs[0] != 0){
        ausgabe_text.innerHTML += text.substring(0, idxs[0])
    }
    for (i=0; i<idxs.length; i++){
        let a = '<tagname style="color:red;">'
        let b = text.substring(idxs[i], idxs[i]+ngram.length)
        let c = '</tagname>'
        let d = ''
        if (i+1 != idxs.length) {
            d = text.substring(idxs[i]+ngram.length, idxs[i+1])
        }
        else {
            d = `${text.substring(idxs[i]+ngram.length)}<br><br>`
        }
        ausgabe_text.innerHTML +=  a + b  + c
        ausgabe_text.innerHTML += d
    }
}