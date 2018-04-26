from main import db

class Tournament(db.Model):
    tournament_id = db.Column(db.Integer, primary_key=True, nullable=False)
    start_day = db.Column(db.Integer, nullable=False)
    prize = db.Column(db.Integer, nullable=False)

    match = db.relationship('Match', backref='tournament')

    @property
    def json(self):
        return {k: getattr(self, k) for k in dir(self) if k[0] != '_' and k not in {'json', 'metadata', 'query', 'query_class'}}
