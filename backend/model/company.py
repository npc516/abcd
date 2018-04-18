from main import db

class Company(db.Model):
    crn = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(64), nullable=False)

