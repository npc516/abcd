from main import db

class Company(db.Model):
    crn = db.Column(db.String(64), primary_key=True, nullable=False)
    name = db.Column(db.String(64), nullable=False)

    policy = db.relationship('Policy', cascade='all,delete')
    sponsorship = db.relationship('Sponsorship', cascade='all,delete')

    @property
    def json(self):
        return {k: getattr(self, k).json if hasattr(getattr(self, k), 'json') else getattr(self, k) for k in [k for k in dir(self) if k[0] != '_' and k not in {'json', 'metadata', 'query', 'query_class'}]}
