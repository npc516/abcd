from main import db

class Policy(db.Model):
    policy_id = db.Column(db.Integer, primary_key=True, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    content = db.Column(db.String(64), nullable=False)

    crn = db.Column(db.String(64), db.ForeignKey('company.crn'), primary_key=True, nullable=False)

    @property
    def json(self):
        return {k: getattr(self, k) for k in dir(self) if k[0] != '_' and k != 'json'}
