from main import db

class User(db.Model):
    email = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    bank_account = db.Column(db.String(64), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(64), nullable=False)
    cats = db.relationship('Cat', backref='owner')

    @property
    def json(self):
        return {'email': self.email,
                'name': self.name,
                'password': self.password,
                'bank_account': self.bank_account,
                'phone': self.phone,
                'address': self.address
                }
