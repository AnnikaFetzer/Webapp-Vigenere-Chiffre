import os

from eingabekontrolle import textanpassung_lower, textanpassung_upper, zahleneingabe
from vigenere_chiffre import encrypt_tabelle, decrypt_tabelle, kasiski, coincidence_berechnung
from vigenere_chiffre import textaufteilung, schluesselberechnung
from grafik import create_diagram

from flask import Blueprint, request, render_template, send_file, flash

# Blueprint definieren
bp_vigenere = Blueprint('bp_vigenere', __name__, template_folder='html', url_prefix='/Vigenere')


@bp_vigenere.route('/')
def hauptseite():
    # Erfolgt ein Seitenaufruf von "http://localhost/Vigenere/" so wird die Seite index.html geladen
    return render_template('index.html')


# ----------------------------------------------------------------------------------------------------------------------
# Verschlüsselung
# ----------------------------------------------------------------------------------------------------------------------
@bp_vigenere.route('/encrypt', methods=['GET'])
def verschluesseln():
    encryptreturn = encrypt_tabelle("rot", "vigenerechiffre")

    # senden der html-Seite verschlüsseln mit einem exemplarischen Schlüssel mit Text und zugehöriger verschlüsselung
    return render_template('verschluesseln.html',
                           keytable=encryptreturn[0],
                           encrypttable=encryptreturn[1],
                           ciphertext=encryptreturn[2],
                           key_param="rot",
                           text_param="vigenerechiffre")


@bp_vigenere.route('/encrypt', methods=['POST'])
def verschluesseln_buttonclick():
    # erfolgt html-Seiten-Eingaben speichern
    texteingabe = request.form.get('cleartext_text').strip()  # strip entfernt Leerzeichen
    schluesseleingabe = request.form.get('key').strip()
    datei = request.files['cleartext_upload']
    fehlereingabe = False

    # Abfangen von Fällen wo das lesen des Dateiinhaltes einem UnicodeDecodeError führt.
    # Kommt es zu diesem Fehler wird die Verschlüsselung an dieser Stelle abgebrochen und somit nicht ausgeführt
    # und eine Nachricht für den Nutzer definiert, welche dann auf der html-Seite ausgegeben werden soll.
    try:
        inhalt = datei.read().decode('utf-8')
    except UnicodeDecodeError:
        flash("Die hochgeladene Datei konnte nicht gelesen werden. Es muss eine .txt Datei hochgeladen werden.")
        return render_template('verschluesseln.html',
                               key_param=schluesseleingabe,
                               text_param=texteingabe,
                               upload_param=datei)

    # zu verwendende Texteingabe überprüfen:

    # Wenn eine Datei geuploadet wurde, wird diese verwendet
    if inhalt != "":
        texteingabe = inhalt

    # bereinigen des Textes auf das Relevante
    texteingabe = textanpassung_lower(texteingabe)

    # überprüfung auf nicht verwertbare Eingabe des zu verschlüsselnden Textes
    if texteingabe == "":
        flash("Es muss ein Text eingegeben oder hochgeladen werden, welcher die Buchstaben a-z enthält!")
        fehlereingabe = True

    # Überprüfung und Bereinigung der Schlüsseleingabe
    schluesseleingabe = textanpassung_lower(schluesseleingabe)
    if schluesseleingabe == "":
        flash("Es muss ein Schlüssel eingegeben werden, welcher die Buchstaben a-z enthält!")
        fehlereingabe = True

    # Behandlung bei fehlerhafter Eingabe:
    # Der Text wird nicht verschlüsselt, es werden nur die Eingaben wieder zurückgegeben
    # und auf der html-Seite der/die Fehler ausgegeben.
    if fehlereingabe:
        return render_template('verschluesseln.html',
                               key_param=schluesseleingabe,
                               text_param=texteingabe,
                               upload_param=datei)

    # Bei richtiger Eingabe
    # wird der Text verschlüsselt und alle zur Darstellung benötigten Informationen an
    # die html-Seite übergeben
    encryptreturn = encrypt_tabelle(schluesseleingabe, texteingabe)

    # senden der html-Seite mit den erfolgten und angepassten Eingaben
    # sowie der erhaltenen Returnwerte der genutzten Funktion
    return render_template('verschluesseln.html',
                           keytable=encryptreturn[0],
                           encrypttable=encryptreturn[1],
                           ciphertext=encryptreturn[2],
                           key_param=schluesseleingabe,
                           text_param=texteingabe,
                           upload_param=datei)


# ----------------------------------------------------------------------------------------------------------------------
# Entschlüsselung
# ----------------------------------------------------------------------------------------------------------------------
@bp_vigenere.route('/decrypt', methods=['GET'])
def entschluesseln():
    # übergebenen String mit dem Schlüssel rot entschlüsseln und das Ergebnis in decrypt_return speichern
    decrypt_return = decrypt_tabelle("rot", "MWZVBXISVYWYWFX")

    # senden der html-Seite mit dem Schlüssel rot, dem verschlüsselten text und dessen Entschlüsselungsergebnis
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
    fehlereingabe = False

    # Abfangen von Fällen wo das lesen des Dateiinhaltes einem UnicodeDecodeError führt.
    # Kommt es zu diesem Fehler wird die Entschlüsselung an dieser Stelle abgebrochen und somit nicht ausgeführt
    # und eine Nachricht für den Nutzer definiert, welche dann auf der html-Seite ausgegeben werden soll.
    try:
        inhalt = datei.read().decode('utf-8')
    except UnicodeDecodeError:
        flash("Die hochgeladene Datei konnte nicht gelesen werden. Es muss eine .txt Datei hochgeladen werden.")
        return render_template('entschluesseln.html',
                               key_param=schluesseleingabe,
                               text_param=texteingabe,
                               upload_param=datei)

    # zu verwendende Texteingabe überprüfen:

    # Wenn eine Datei geuploadet wurde, wird diese verwendet
    if inhalt != "":
        texteingabe = inhalt

    # bereinigen des Textes auf das Relevante
    texteingabe = textanpassung_upper(texteingabe)

    # überprüfung auf nicht verwertbare Eingabe
    if texteingabe == "":
        flash("Es muss ein Text eingegeben oder hochgeladen werden, welcher die Buchstaben a-z enthält!")
        fehlereingabe = True

    # Überprüfung und Bereinigung der Schlüsseleingabe
    schluesseleingabe = textanpassung_lower(schluesseleingabe)
    if schluesseleingabe == "":
        flash("Es muss ein Schlüssel eingegeben werden, welcher die Buchstaben a-z enthält!")
        fehlereingabe = True

    # Behandlung bei fehlerhafter Eingabe:
    # der Text wird nicht entschlüsselt, es werden nur die Eingaben wieder zurückgegeben
    # und dann auf der html-Seite der/die Fehler ausgegeben.
    if fehlereingabe:
        return render_template('entschluesseln.html',
                               key_param=schluesseleingabe,
                               text_param=texteingabe,
                               upload_param=datei)

    # Bei richtiger Eingabe
    # wird der Text entschlüsselt und alle zur Darstellung benötigten Informationen an
    # die html-Seite übergeben
    decrypt_return = decrypt_tabelle(schluesseleingabe, texteingabe)

    # senden der html-Seite mit den zuvor erfolgten Eingaben sowie den berechneten Returnwerten
    return render_template('entschluesseln.html',
                           keytable=decrypt_return[0],
                           decrypttable=decrypt_return[1],
                           cleartext=decrypt_return[2],
                           key_param=schluesseleingabe,
                           text_param=texteingabe,
                           upload_param=datei)


# ----------------------------------------------------------------------------------------------------------------------
# Kasiski-Test
# ----------------------------------------------------------------------------------------------------------------------
@bp_vigenere.route('/kasiski', methods=['GET'])
def kasiski_test():
    # senden der html-Seite kasiki-test.html
    return render_template('kasiski-test.html')


@bp_vigenere.route('/kasiski', methods=['POST'])
def kasiski_test_buttonclick():
    # die Eingabevariablen aus der html-Seite werden in ng_lenth, teixteingabe und datei gespeichert
    ng_length = request.form.get('ngramm_length').strip()
    texteingabe = request.form.get('cipher_text').strip()
    datei = request.files.get('ciphertext_upload')

    fehlereingabe = False

    # Abfangen von Fällen wo das lesen des Dateiinhaltes einem UnicodeDecodeError führt.
    # Kommt es zu diesem Fehler wird die n-gramm-Suche an dieser Stelle abgebrochen und somit nicht ausgeführt
    # und eine Nachricht für den Nutzer definiert, welche dann auf der html-Seite ausgegeben werden soll.
    try:
        dateiinhalt = datei.read().decode('utf-8')
    except UnicodeDecodeError:
        flash("Die hochgeladene Datei konnte nicht gelesen werden. Es muss eine .txt Datei hochgeladen werden.")
        return render_template('kasiski-test.html',
                               ngramm_param=ng_length,
                               text_param=texteingabe)

    # zu verwendende Texteingabe überprüfen:
    # Wenn eine Datei geuploadet wurde, wird diese verwendet
    # Das was im Texteingabefeld steht wird dann nicht weiter beachtet
    if dateiinhalt != "":
        texteingabe = dateiinhalt
    # bereinigen des Textes auf das Relevante
    texteingabe = textanpassung_upper(texteingabe)
    # überprüfung auf nicht verwertbare Eingabe
    if texteingabe == "":
        flash("Es muss ein Text eingegeben oder hochgeladen werden, welcher die Buchstaben a-z enthält!")
        fehlereingabe = True

    # Überprüfung der Eingabe für die n-gramm-Länge
    ng_length = zahleneingabe(ng_length, False)
    if ng_length == -1:
        flash("Es muss eine Ganzzahl eingebenen werden, "
              "welche besagt, nach welcher n-gramm Länge im Text gesucht werden soll!")
        fehlereingabe = True

    # Behandlung bei fehlerhafter Eingabe:
    # der Text wird nicht auf n-gramme untersucht, es werden nur die Eingaben wieder zurückgegeben
    # und auf der html-Seite der/die Fehler ausgegeben.
    if fehlereingabe:
        return render_template('kasiski-test.html',
                               text_param=texteingabe)

    # Suche nach n-grammen
    kasiski_return = kasiski(texteingabe, int(ng_length))

    # Anzahl wie viele n-Gramme gefunden wurden
    anzahl = len(kasiski_return[0])

    # senden der html-Seite mit den erfolgten Eingaben, dem erhaltenen Return des
    # Funktionsaufrufres und der berechneten Anzahl
    return render_template('kasiski-test.html',
                           ngramme=kasiski_return[0],
                           gcd=kasiski_return[1],
                           text_param=texteingabe,
                           ng_anzahl=anzahl)


@bp_vigenere.route('/kasiski_js_send', methods=['GET'])
def kasiski_js_send():
    # senden des Javascriptfiles kasiski.js
    return send_file(os.path.join(os.path.dirname(os.path.relpath(__file__)), 'kasiski.js'))


# ----------------------------------------------------------------------------------------------------------------------
# Koinzidenzindex
# ----------------------------------------------------------------------------------------------------------------------
@bp_vigenere.route('/koinzidenzindex', methods=['GET'])
def koinzidenzindex_methode():
    # senden der html-Seite koinzidenzindex-methode.html
    return render_template('koinzidenzindex-methode.html')


@bp_vigenere.route('/koinzidenzindex', methods=['POST'])
def koinzidenzindex_methode_buttonclick():
    # Die Eingaben der html-Seite in Variablen speichern
    max_cols = request.form.get('cols_number').strip()
    threshold = request.form.get('threshold').strip()
    texteingabe = request.form.get('cipher_text').strip()
    datei = request.files.get('ciphertext_upload')

    fehlereingabe = False

    # Abfangen von Fällen wo das Lesen des Dateiinhaltes einem UnicodeDecodeError führt.
    # Kommt es zu diesem Fehler wird die Koinzidenindexberechnung an dieser Stelle abgebrochen
    # und eine Nachricht für den Nutzer definiert, welche dann auf der html-Seite ausgegeben werden soll.
    try:
        dateiinhalt = datei.read().decode('utf-8')
    except UnicodeDecodeError:
        flash("Die hochgeladene Datei konnte nicht gelesen werden. Es muss eine .txt Datei hochgeladen werden.")
        return render_template('koinzidenzindex-methode.html',
                               cols_param=max_cols,
                               threshold_param=threshold,
                               text_param=texteingabe)

    # zu verwendende Texteingabe überprüfen:
    # Wenn eine Datei hochgeladen wurde, wird diese verwendet.
    # Das, was im Texteingabefeld steht, wird dann nicht weiter beachtet.
    if dateiinhalt != "":
        texteingabe = dateiinhalt
    # bereinigen des Textes auf das Relevante
    texteingabe = textanpassung_upper(texteingabe)
    # überprüfung auf nicht verwertbare Eingabe
    if texteingabe == "":
        flash("Es muss ein Text eingegeben oder hochgeladen werden, welcher die Buchstaben a-z enthält!")
        fehlereingabe = True

    # Überprüfung der Eingabe für maximal zu betrachtende Spaltenanzahl
    max_cols = zahleneingabe(max_cols, False)
    if max_cols == -1:
        flash("Bei der Schlüssellänge/Spaltenanzahl muss eine Ganzzahl eingebenen werden, "
              "welche besagt, in bis zu wie viele Spalten der Text aufgeteilt werden soll!")
        fehlereingabe = True

    if threshold != "":
        # Überprüfung der Eingabe für den Schwellwert
        threshold = zahleneingabe(threshold, True)

        # ist der threshold nun -1 ist eine falsche Eingabe erfolgt und es wird eine Fehlermeldung ausgegeben
        if threshold == -1:
            flash("Beim Schwellwert muss eine Kommazahl mit einem Punkt als Trennzeichen eingebenen werden!")
            fehlereingabe = True
    # Wenn zum Schwellwert keine Eingabe erfolgt ist, wird threshold auf den defaultwert 0.065 gesetzt
    else:
        threshold = "0.065"

    # Behandlung bei fehlerhafter Eingabe:
    # Für die verschiedenen Spalten werden die Koinzidenzindexe nicht berechnet,
    # es werden nur die Eingaben wieder zurückgegeben und auf der html-Seite der/die Fehler ausgegeben.
    if fehlereingabe:
        return render_template('koinzidenzindex-methode.html',
                               cols_param=max_cols,
                               threshold_param=threshold,
                               text_param=texteingabe)

    # Berechnung der Koinzidenzindexe
    ci_return = coincidence_berechnung(str(texteingabe), int(max_cols), float(threshold))

    # sender der html-Seite mit den erfolgten Eingaben und den berechneten Koinzidenzindexen
    return render_template('koinzidenzindex-methode.html',
                           cols_param=max_cols,
                           threshold_param=float(threshold),
                           text_param=texteingabe,
                           ki_tabelle=ci_return)


@bp_vigenere.route('/ci_js_send', methods=['GET'])
def ci_js_send():
    # senden des Javascriptfiles ki_spaltenaufteilung.js
    return send_file(os.path.join(os.path.dirname(os.path.relpath(__file__)), 'ki_spaltenaufteilung.js'))


# ----------------------------------------------------------------------------------------------------------------------
# Schlüsselberechnung
# ----------------------------------------------------------------------------------------------------------------------
@bp_vigenere.route('/gegenseitigerKoinzidenzindex', methods=['GET'])
def gki_methode():
    # senden der html-Seite schluesselberechnung.html
    return render_template('schluesselberechnung.html')


@bp_vigenere.route('/gegenseitigerKoinzidenzindex', methods=['POST'])
def gki_methode_buttonclick():
    # Die Eingaben der html-Seite in Variablen speichern
    cols = request.form.get('keylength')
    threshold = request.form.get('schwellwert')
    texteingabe = request.form.get('cipher_text')
    datei = request.files.get('ciphertext_upload')

    fehlereingabe = False

    # Abfangen von Fällen wo das Lesen des Dateiinhaltes einem UnicodeDecodeError führt.
    # Kommt es zu diesem Fehler wird die Schlüsselberechnung an dieser Stelle abgebrochen
    # und stattdessen eine Nachricht für den Nutzer definiert, welche dann auf der html-Seite ausgegeben werden soll.
    try:
        dateiinhalt = datei.read().decode('utf-8')
    except UnicodeDecodeError:
        flash("Die hochgeladene Datei konnte nicht gelesen werden. Es muss eine .txt Datei hochgeladen werden.")
        return render_template('schluesselberechnung.html',
                               text_param=texteingabe,
                               schwellwert_param=threshold,
                               keylength_param=cols,
                               cols=int(cols))

    # zu verwendende Texteingabe überprüfen:
    # Wenn eine Datei hochgeladen wurde, wird diese verwendet.
    # Das, was im Texteingabefeld steht, wird dann nicht weiter beachtet.
    if dateiinhalt != "":
        texteingabe = dateiinhalt
    # Bereinigen des Textes auf das Relevante
    texteingabe = textanpassung_upper(texteingabe)
    # überprüfung leere, bzw. falsche Eingabe
    if texteingabe == "":
        flash("Es muss ein Text eingegeben oder hochgeladen werden, welcher die Buchstaben a-z enthält!")
        fehlereingabe = True

    if threshold != "":
        # Überprüfung der Eingabe für den Schwellwert
        threshold = zahleneingabe(threshold, True)

        # ist der threshold nun -1, ist eine falsche Eingabe erfolgt und es wird eine Fehlermeldung ausgegeben
        if threshold == -1:
            flash("Beim Schwellwert muss eine Kommazahl mit einem Punkt als Trennzeichen eingebenen werden!")
            fehlereingabe = True
    # Wenn zum Schwellwert keine Eingabe erfolgt ist, wird threshold auf den Defaultwert 0.065 gesetzt
    else:
        threshold = "0.065"

    # Überprüfung der Eingabe für die Spaltenanzahl
    cols = zahleneingabe(cols, False)
    if cols == -1:
        flash("Bei der Schlüssellänge/Spaltenanzahl muss eine Ganzzahl eingebenen werden!")
        fehlereingabe = True

    # Behandlung bei fehlerhafter Eingabe:
    # Die Schlüsselberechnung wird an dieser Stelle abgebrochen.
    # Die in der html-Seite erfolgten Eingaben werden an schluesselberechnung.html übergeben.
    # Zudem können die mit flash erfolgten Fehlermeldungen auf der html-Seite ausgegeben werden.
    if fehlereingabe:
        return render_template('schluesselberechnung.html',
                               text_param=texteingabe,
                               schwellwert_param=threshold,
                               keylength_param=cols,
                               cols=int(cols))

    # Aufteilung des Textes in texteingabe in so viele Texte/Spalten wie in der Variable cols festgelegt
    texte = textaufteilung(texteingabe, int(cols))

    # Hinzufügen der Indexe der jeweiligen Texte für die Ausgabe in html
    texttabelle = []
    for i in range(int(cols)):
        texttabelle.append([i + 1, texte[i]])

    # Berechnung der möglichen Schlüssel
    sb_return = schluesselberechnung(texteingabe, texte, int(cols), float(threshold))

    return render_template('schluesselberechnung.html',
                           text_param=texteingabe,
                           schwellwert_param=float(threshold),
                           keylength_param=cols,
                           cols=int(cols),
                           texte=texttabelle,
                           mics=sb_return[0],
                           matrix=sb_return[1],
                           schluessel=sb_return[2])


@bp_vigenere.route('/schluessel_js_send', methods=['GET'])
def schluessel_js_send():
    # senden des Javascriptfiles schlussel.js
    return send_file(os.path.join(os.path.dirname(os.path.relpath(__file__)), 'schluessel.js'))


@bp_vigenere.route('/matplotimage', methods=['GET'])
def matplotimage():
    # Inhalt aus der Url in den Variabeln abspeichern
    text1 = request.args.get("text1")
    text2 = request.args.get("text2")
    shift = request.args.get("shift")

    # Diagramm mithilfe der Variablen erzeugen und dieses an die html-Datei senden
    diagram = create_diagram(text1, text2, int(shift))
    return send_file(diagram)
