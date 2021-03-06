from main import db

class RatingFee(db.Model):
    rating = db.Column(db.Integer, primary_key=True, nullable=False)
    fee = db.Column(db.Float, nullable=False)

    trainer = db.relationship('Trainer')

    @property
    def json(self):
        return {k: getattr(self, k).json if hasattr(getattr(self, k), 'json') else getattr(self, k) for k in [k for k in dir(self) if k[0] != '_' and k not in {'json', 'metadata', 'query', 'query_class'}]}
