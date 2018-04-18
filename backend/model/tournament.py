from main import db

class Tournament(db.Model):
    tournament_id = db.Column(db.Integer, primary_key=True)
    start_day = db.Column(db.Integer, nullable=False)
    prize = db.Column(db.Integer, nullable=False)
