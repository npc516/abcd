from main import db

class Match(db.Model):
    event_id = db.Column(db.Integer, primary_key=True, nullable=False)
    location = db.Column(db.String(64), nullable=False)
    day = db.Column(db.Integer, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    result = db.Column(db.Integer, nullable=True)

    tournament_id = db.Column(db.Integer, db.ForeignKey('tournament.tournament_id'), nullable=False)
    cat1_id = db.Column(db.Integer, db.ForeignKey('cat.cat_id'), nullable=False)
    cat2_id = db.Column(db.Integer, db.ForeignKey('cat.cat_id'), nullable=False)

    @property
    def json(self):
        return {k: getattr(self, k) for k in dir(self) if k[0] != '_' and k != 'json'}
