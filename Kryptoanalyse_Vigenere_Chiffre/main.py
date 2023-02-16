
from flask import Flask, send_file, render_template

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


# localer Server auf port 80 starten
webapp.run(host='localhost', port=80)
