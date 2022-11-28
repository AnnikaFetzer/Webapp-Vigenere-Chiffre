

from Encrypt import encrypt_tabelle
from VigenereChiffre import decrypt_tabelle

from flask import Blueprint, url_for, redirect, request, render_template, send_file
# from matplotlib.backends.backend_template import FigureCanvas


bp_vigenere = Blueprint('bp_vigenere', __name__, template_folder='html', url_prefix='/Vigenere')


# ----------------------------------------------------------------------------------------------------------------------
# Verschlüsselung
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
    inhalt = datei.read().decode('utf-8')

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
    # todo: parallellnutzung (andere Lösung, atomatischer Download bei berechnung, neues berechnen von ciphertext hier?
    return send_file('decrypttext.txt', as_attachment=True)

# ----------------------------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------------------------


@bp_vigenere.route('kasiski', methods=['GET'])
def kasiski_test():
    # texteingabe = request.form.get('cipher_text')
    # datei = request.files.get('ciphertext_upload')
    return render_template('kasiski-test.html')


@bp_vigenere.route('koinzidenzindex', methods=['GET'])
def koinzidenzindex_methode():
    return render_template('koinzidenzindex-methode.html')
