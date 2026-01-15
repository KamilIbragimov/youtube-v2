import os
from flask import Flask



#prendiamo cartella istanza
app = Flask(__name__, instance_relative_config=True)

app.config.from_mapping(
        # SECRET_KEY serve a Flask per firmare i dati sicuri (es. sessioni).
        # 'dev' va bene per sviluppare, ma in produzione andrà cambiata.
        SECRET_KEY='dev',
        # Diciamo a Flask dove salvare il file del database SQLite
        DATABASE=os.path.join(app.instance_path, 'Arlotti.sqlite'),
    )
# Assicuriamoci che la cartella instance esista



from . import db
db.init_app(app)



# --- REGISTRAZIONE BLUEPRINTS ---