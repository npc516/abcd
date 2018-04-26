from main import db

class Sponsorship(db.Model):
    sponsorship_id = db.Column(db.Integer, primary_key=True, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    payment = db.Column(db.Integer, nullable=False)
    content = db.Column(db.String(64), nullable=False)

    crn = db.Column(db.String(64), db.ForeignKey('company.crn'), primary_key=True, nullable=False)

    @property
    def json(self):
        return {k: getattr(self, k).json if hasattr(getattr(self, k), 'json') else getattr(self, k) for k in [k for k in dir(self) if k[0] != '_' and k not in {'json', 'metadata', 'query', 'query_class'}]}
