
from flask import Flask

from blueprints import bp_vigenere


webapp = Flask("Kryptoanalyse der Vigenere Chiffre")
webapp.config['SECRET_KEY'] = 'geheimer Schluessel'
webapp.template_folder = 'html'
webapp.register_blueprint(bp_vigenere)

webapp.run(host='localhost', port=80)



