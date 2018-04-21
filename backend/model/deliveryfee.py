from main import db

class DeliveryFee(db.Model):
    destination = db.Column(db.String(64), primary_key=True, nullable=False)
    current_location = db.Column(db.String(64), primary_key=True, nullable=False)
    fee = db.Column(db.Integer, nullable=False)

    delivery = db.relationship('Delivery', backref='delivery_fee')

    @property
    def json(self):
        return {k: getattr(self, k) for k in dir(self) if k[0] != '_' and k != 'json'}
