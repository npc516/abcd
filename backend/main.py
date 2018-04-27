from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import event

app = Flask('UCC')
CORS(app)
app.config.from_object('config')
db = SQLAlchemy(app)
event.listen(db.engine, 'connect', lambda x, y: x.execute('pragma foreign_keys=on'))

from api import *

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
