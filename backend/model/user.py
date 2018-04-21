from main import db

class User(db.Model):
    email = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    bank_account = db.Column(db.String(64), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(64), nullable=False)

    cat = db.relationship('Cat', backref='owner')
    comment = db.relationship('Comment', backref='commenter')

    @property
    def json(self):
        return {k: getattr(self, k) for k in dir(self) if k[0] != '_' and k != 'json'}
