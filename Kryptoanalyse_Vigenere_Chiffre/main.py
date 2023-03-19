
from flask import Flask, send_file, render_template
from werkzeug.exceptions import HTTPException

from blueprints import bp_vigenere


webapp = Flask("Kryptoanalyse der Vigenere Chiffre")
webapp.config['SECRET_KEY'] = 'geheimer Schluessel'
webapp.template_folder = 'html'
webapp.register_blueprint(bp_vigenere)


@webapp.route('/')
def hauptseite():
    # bei Aufruf von localhost wird die Seite index.html geladen
    return render_template('index.html')


@webapp.route('/hs-aalen.svg', methods=['GET'])
def hs_logo():
    return send_file('hs-aalen.svg', as_attachment=True)


@webapp.errorhandler(Exception)
def handle_exception(e):
    # pass through HTTP errors
    if isinstance(e, HTTPException):
        # HTTP Fehlercodes an Nutzer weiterleiten
        return render_template('fehler.html',
                               error_name=e.name,
                               error_description=e.description)

    # es ist ein Fehler im code aufgetreten -> diesen vor dem Nutzer verbergen
    return render_template('fehler.html',
                           error_name='Internal Server Error',
                           error_description='The server encountered an internal error and was unable to complete your '
                                             'request.')


# localer Server auf port 80 starten
webapp.run(host='localhost', port=8080)
