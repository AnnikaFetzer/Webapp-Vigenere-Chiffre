
from VigenereChiffre import encrypt_tabelle, decrypt_tabelle, kasiski, coincidence_berechnung
from VigenereChiffre import textaufteilung, schluesselberechnung, textanpassung_upper
from grafik import create_diagram

from flask import Blueprint, url_for, redirect, request, render_template, send_file, flash

# from matplotlib.backends.backend_template import FigureCanvas


bp_vigenere = Blueprint('bp_vigenere', __name__, template_folder='html', url_prefix='/Vigenere')


# ----------------------------------------------------------------------------------------------------------------------
# Verschlüsselung
#  <input type="textarea" id="cipher_text" name="cipher_text" value="{{text_param}}"><br>
# ----------------------------------------------------------------------------------------------------------------------
@bp_vigenere.route('/')
def hauptseite():
    return redirect(url_for('bp_vigenere.verschluesseln'))


@bp_vigenere.route('/encrypt', methods=['GET'])
def verschluesseln():

    encryptreturn = encrypt_tabelle("rot", "vigenerechiffre")

    return render_template('verschluesseln.html',
                           keytable=encryptreturn[0],
                           encrypttable=encryptreturn[1],
                           ciphertext=encryptreturn[2],
                           key_param="rot",
                           text_param="vigenerechiffre")


@bp_vigenere.route('/encrypt', methods=['POST'])
def verschluesseln_buttonclick():

    texteingabe = request.form.get('cleartext_text').strip()  # strip entfert leerzeichen
    schluesseleingabe = request.form.get('key').strip()
    datei = request.files['cleartext_upload']

    # macht keine exception, wenn datei nicht existiert (gibt dann None zurück)
    # request.files.get('cleartext_upload526126')

    # variante 1
    # file.save('pfadzurdatei.txt')
    # with open('pfadzurdatei.txt') as f:
    #     inhalt = f.read()

    # variante 2
    inhalt = datei.read().decode('utf-8')

    if inhalt == "":
        encryptreturn = encrypt_tabelle(schluesseleingabe, texteingabe)

    else:
        encryptreturn = encrypt_tabelle(schluesseleingabe, inhalt)

    return render_template('verschluesseln.html',
                           keytable=encryptreturn[0],
                           encrypttable=encryptreturn[1],
                           ciphertext=encryptreturn[2],
                           key_param=schluesseleingabe,
                           text_param=texteingabe,
                           upload_param=datei)


@bp_vigenere.route('/encrypt_download', methods=['GET'])
def encrypt_download_file():
    # todo: parallellnutzung (andere Lösung, atomatischer Download bei berechnung, neues berechnen von ciphertext hier?
    return send_file('encrypttext.txt', as_attachment=True)


# ----------------------------------------------------------------------------------------------------------------------
# Entschlüsselung
# ----------------------------------------------------------------------------------------------------------------------
@bp_vigenere.route('/decrypt', methods=['GET'])
def entschluesseln():

    decrypt_return = decrypt_tabelle("rot", "MWZVBXISVYWYWFX")

    return render_template('entschluesseln.html',
                           keytable=decrypt_return[0],
                           decrypttable=decrypt_return[1],
                           cleartext=decrypt_return[2],
                           key_param="rot",
                           text_param="MWZVBXISVYWYWFX")


@bp_vigenere.route('/decrypt', methods=['POST'])
def entschluesseln_buttonclick():

    texteingabe = request.form.get('cipher_text')
    schluesseleingabe = request.form.get('key')
    datei = request.files['ciphertext_upload']
    # todo handel UnicodeDecodeError -> Fehler ausgeben
    inhalt = datei.read().decode('utf-8')


    if schluesseleingabe == "":
        flash("Es muss ein Schlüssel eingegeben werden!")
        return render_template('entschluesseln.html',
                               key_param=schluesseleingabe,
                               text_param=texteingabe,
                               upload_param=datei)

    else:

        if inhalt == "":
            decrypt_return = decrypt_tabelle(schluesseleingabe, texteingabe)

        else:
            decrypt_return = decrypt_tabelle(schluesseleingabe, inhalt)



    return render_template('entschluesseln.html',
                           keytable=decrypt_return[0],
                           decrypttable=decrypt_return[1],
                           cleartext=decrypt_return[2],
                           key_param=schluesseleingabe,
                           text_param=texteingabe,
                           upload_param=datei)


@bp_vigenere.route('/decrypt_download', methods=['GET'])
def decrypt_download_file():
    # todo: parallellnutzung (andere Lösung, automatischer Download bei berechnung, neues berechnen von ciphertext hier?

    test = request.args
    cleartext = request.args.get("text")

    return send_file('decrypttext.txt', as_attachment=True)


# ----------------------------------------------------------------------------------------------------------------------
# Kasiski-Test
# ----------------------------------------------------------------------------------------------------------------------
@bp_vigenere.route('/kasiski', methods=['GET'])
def kasiski_test():
    return render_template('kasiski-test.html')


@bp_vigenere.route('/kasiski', methods=['POST'])
def kasiski_test_buttonclick():
    ng_length = request.form.get('ngramm_length')
    texteingabe = request.form.get('cipher_text')
    datei = request.files.get('ciphertext_upload')
    dateiinhalt = datei.read().decode('utf-8')

    # Todo: abfangen wenn keine/falsche Eingabe der n-gramm-Länge erfolgt ist
    # Todo: besseres abfangen wenn keine Eingabe -> Fehlermeldung
    if dateiinhalt == "" and texteingabe == "":
        texteingabe = "MOIRBMOVOXBUEARWALSPHTIHFAPIFNDXMMNMOIPYXLHWAZZXOEMOICYWTIBZNAXSEXKXVNMPXCZXUHSQBSPPHMKESAXY"
        kasiski_return = kasiski(texteingabe, int(ng_length))
    # Wenn keine Datei hochgeladen wurde, wird kasiski mit Texteingabe aufrufen
    elif dateiinhalt == "":
        texteingabe = textanpassung_upper(texteingabe)
        kasiski_return = kasiski(texteingabe, int(ng_length))
    # ansonsten wird kasiski mit dem Dateiinhalt aufgerufen
    else:
        dateiinhalt = textanpassung_upper(dateiinhalt)
        kasiski_return = kasiski(dateiinhalt, int(ng_length))
        texteingabe = dateiinhalt

    # Anzahl wie viele n-Gramme gefunden wurden
    anzahl = len(kasiski_return[0])

    return render_template('kasiski-test.html',
                           ngramme=kasiski_return[0],
                           gcd=kasiski_return[1],
                           ngramm_param=ng_length,
                           text_param=texteingabe,
                           ng_anzahl=anzahl)


@bp_vigenere.route('/kasiski_js_send', methods=['GET'])
def kasiski_js_send():
    return send_file('kasiski.js')


# ----------------------------------------------------------------------------------------------------------------------
# Koinzidenzindex
# ----------------------------------------------------------------------------------------------------------------------
@bp_vigenere.route('/koinzidenzindex', methods=['GET'])
def koinzidenzindex_methode():
    test = "UHDJVMBBNFBUKOSYZTFUACBQMIOAUECIFZBCTHANTANEQQPGNTISKBSCSEZBRJBZCGCPQLPRQMNTDCIKTCXAEYAWGNOGWGWZYESVOO"
    coincidence_berechnung(test, int(4), float(0.65))
    return render_template('koinzidenzindex-methode.html')


@bp_vigenere.route('/koinzidenzindex', methods=['POST'])
def koinzidenzindex_methode_buttonclick():
    max_cols = request.form.get('cols_number')
    threshold = request.form.get('threshold')
    texteingabe = request.form.get('cipher_text')
    datei = request.files.get('ciphertext_upload')
    dateiinhalt = datei.read().decode('utf-8')

    if threshold == "":
        threshold = "0.065"
    if max_cols == "":
        max_cols = 10

    # Todo: abfangen wenn leerer/falscher Eingaben
    # Todo: besseres abfangen wenn keine Eingabe -> Fehlermeldung
    if dateiinhalt == "" and texteingabe == "":
        texteingabe = "MOIRBMOVOXBUEARWALSPHTIHFAPIFNDXMMNMOIPYXLHWAZZXOEMOICYWTIBZNAXSEXKXVNMPXCZXUHSQBSPPHMKESAXY"
        ci_return = coincidence_berechnung(str(texteingabe), int(max_cols), float(threshold))
    # Wenn keine Datei hochgeladen wurde, wird kasiski mit Texteingabe aufrufen
    elif dateiinhalt == "":
        ci_return = coincidence_berechnung(str(texteingabe), int(max_cols), float(threshold))
    # ansonsten wird kasiski mit dem Dateiinhalt aufgerufen
    else:
        ci_return = coincidence_berechnung(str(dateiinhalt), int(max_cols), float(threshold))
        texteingabe = dateiinhalt

    return render_template('koinzidenzindex-methode.html',
                           cols_param=max_cols,
                           threshold_param=threshold,
                           text_param=texteingabe,
                           ki_tabelle=ci_return)


@bp_vigenere.route('/ci_js_send', methods=['GET'])
def ci_js_send():
    return send_file('ki_spaltenaufteilung.js')


# ----------------------------------------------------------------------------------------------------------------------
# Schlüsselberechnung
# ----------------------------------------------------------------------------------------------------------------------
@bp_vigenere.route('/gegenseitigerKoinzidenzindex', methods=['GET'])
def gki_methode():
    return render_template('schluesselberechnung.html')


@bp_vigenere.route('/gegenseitigerKoinzidenzindex', methods=['POST'])
def gki_methode_buttonclick():

    cols = request.form.get('keylength')
    threshold = request.form.get('schwellwert')
    texteingabe = request.form.get('cipher_text')
    datei = request.files.get('ciphertext_upload')
    dateiinhalt = datei.read().decode('utf-8')

    # Todo: abfangen wenn keine/falsche Eingabe der n-gramm-Länge erfolgt ist
    # Todo: besseres abfangen wenn keine Eingabe -> Fehlermeldung

    if threshold == "":
        threshold = 0.065

    # todo: was wenn beides leer?
    if dateiinhalt == "":
        texte = textaufteilung(texteingabe, int(cols))
    else:
        texte = textaufteilung(dateiinhalt, int(cols))
        texteingabe = dateiinhalt

    texttabelle = []
    for i in range(int(cols)):
        texttabelle.append([i+1, texte[i]])

    # mutual_coincidence_index(texte[0], texte[1])
    sb_return = schluesselberechnung(texteingabe, texte, int(cols), float(threshold))

    return render_template('schluesselberechnung.html',
                           text_param=texteingabe,
                           schwellwert_param=threshold,
                           keylength_param=cols,
                           cols=int(cols),
                           texte=texttabelle,
                           mics=sb_return[0],
                           matrix=sb_return[1],
                           schluessel=sb_return[2])


@bp_vigenere.route('/schluessel_js_send', methods=['GET'])
def schluessel_js_send():
    return send_file('schluessel.js')


@bp_vigenere.route('/matplotimage', methods=['GET'])
def matplotimage():
    test = request.args
    text1 = request.args.get("text1")
    text2 = request.args.get("text2")
    shift = request.args.get("shift")

    fname = create_diagram(text1, text2, int(shift))

    return send_file(fname)
