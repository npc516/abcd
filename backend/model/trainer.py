from main import db

class Trainer(db.Model):
    ssn = db.Column(db.String(64), primary_key=True, nullable=False)
    license = db.Column(db.String(64), nullable=False)
    name = db.Column(db.String(64), nullable=False)
    routine = db.Column(db.String(64), nullable=False)
    experience = db.Column(db.Integer, nullable=True)

    rating = db.Column(db.Integer, db.ForeignKey('ratingfee.rating'))

    @property
    def json(self):
        return {k: getattr(self, k) for k in dir(self) if k[0] != '_' and k != 'json'}
