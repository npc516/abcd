from main import db

class Audition(db.Model):

    event_id = db.Column(db.Integer, primary_key=True, nullable=False)
    location = db.Column(db.String(64), nullable=False)
    start_day = db.Column(db.Integer, nullable=False)
    entry_fee = db.Column(db.Integer, nullable=False)
    duration = db.Column(db.Integer, nullable=False)

    @property
    def json(self):
        return {k: getattr(self, k) for k in dir(self) if k[0] != '_' and k not in {'json', 'metadata', 'query', 'query_class'}}
