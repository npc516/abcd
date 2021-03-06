from main import db

class Trainer(db.Model):
    ssn = db.Column(db.String(64), primary_key=True, nullable=False)
    license = db.Column(db.String(64), nullable=False)
    name = db.Column(db.String(64), nullable=False)
    routine = db.Column(db.String(64), nullable=False)
    experience = db.Column(db.Integer, nullable=True)

    rating = db.Column(db.Integer, db.ForeignKey('rating_fee.rating'))

    @property
    def json(self):
        return {k: getattr(self, k).json if hasattr(getattr(self, k), 'json') else getattr(self, k) for k in [k for k in dir(self) if k[0] != '_' and k not in {'json', 'metadata', 'query', 'query_class'}]}
