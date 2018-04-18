from main import db

class Match(db.Model):
    event_id = db.Column(db.Integer, primary_key=True, nullable=False)
    location = db.Column(db.String(64), nullable=False)
    day = db.Column(db.Integer, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    result = db.Column(db.Integer, nullable=True)
