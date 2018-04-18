from main import db

class Audition(db.Model):
    event_id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(64), nullable=False)
    start_day = db.Column(db.Integer, nullable=False)
    entry_fee = db.Column(db.Integer, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
