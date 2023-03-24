# Webapp-Vigenere-Chiffre

## Installation

Für die Ausführung der Webanwendung ist eine Python-Installation erforderlich. 

Die Anwendung wurde mit Python 3.10 entwickelt. 

Die folgenden Befehle sind im ``root``-Verzeichnis des Projekts auszuführen.


### Erstellen einer virtuellen Python-Umgebung (optional)

Virtuelle Python-Umgebungen erlauben die Abhängigkeiten für ein bestimmtes Projekt zu installieren. 
Der System-Interpreter und alle anderen Projekte bleiben davon unberührt.

Zunächst muss sichergestellt sein, dass das Paket für virtuelle Umgebungen installiert ist:

```
pip install virtualenv
```

Virtuelle Umgebung erstellen (im Verzeichnis ``virtual_environment``):

```
python -m venv virtual_environment
```

Anschließend die virtuelle Umgebung aktivieren:

Windows:

```
virtual_environment/Scripts/activate
```

Linux:

```
. virtual_environment/bin/activate
```

### Installieren der Projekt-Abhängigkeiten

Die Abhängigkeiten des Projekts werden durch den folgen Befehl installiert:

```
pip install -r ./requirements.txt
```

### Ausführen der Webanwendung

Ausgeführt wird die Anwendung durch den Befehl

```
python ./kryptoanalyse_vigenere_chiffre/main.py 
```

Solle die Ausführung blockiert werden, da der Port 80 bereits verwendet wird, kann der Port in der Datei 
``./kryptoanalyse_vigenere_chiffre/main.py `` angepasst werden
