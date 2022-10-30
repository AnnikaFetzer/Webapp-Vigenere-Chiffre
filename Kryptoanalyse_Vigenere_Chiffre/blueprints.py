

from Encrypt import encrypt_tabelle

from flask import Blueprint, url_for, redirect, request, render_template, send_file, Response
from matplotlib.backends.backend_template import FigureCanvas



bp_vigenere = Blueprint('bp_vigenere', __name__, template_folder='html', url_prefix='/Vigenere')



@bp_vigenere.route('/')
def hauptseite():
    return redirect(url_for('bp_vigenere.verschluesseln'))

@bp_vigenere.route('/encrypt', methods=['GET'])
def verschluesseln():

    # if args:
    #     list = encrypt_tabelle("rot", args[0])
    # else:
    #return "Hallo Welt", 200
    #tabelle = encrypt_tabelle("rot", "abc defgHIJ klMnOpqrstuvwxyz127")
    encryptreturn = encrypt_tabelle("rot", "vigenerechiffre")

    from flask import session

    return render_template('verschluesseln.html',
                           keytable=encryptreturn[0],
                           encrypttable=encryptreturn[1],
                           ciphertext=encryptreturn[2],
                           key_param="rot",
                           text_param="vigenerechiffre")



@bp_vigenere.route('/encrypt', methods=['POST'])
def verschluesseln_buttonclick():

    texteingabe = request.form.get('cleartext_text').strip() #strip entfert leerzeichen
    schluesseleingabe = request.form.get('key').strip()
    dateiname = request.form.get('cleartext_upload')
    datei = request.files['cleartext_upload']

    # macht keine exception wenn datei nicht existiert (gibt dann None zurück)
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

@bp_vigenere.route('/download', methods=['GET'])
def download_file():
    #todo: parallellnutzung (andere Lösung, atomatischer Download bei berechnung, neues berechnen von ciphertext hier?
    return send_file('encrypttext.txt', as_attachment=True)
