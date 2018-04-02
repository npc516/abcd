from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask('UCC')
CORS(app)
app.config.from_object('config')
db = SQLAlchemy(app)

from api import *

if __name__ == '__main__':
    app.run(debug=True)
