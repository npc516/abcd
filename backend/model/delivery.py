from main import db

class Delivery(db.Model):
    delivery_id = db.Column(db.Integer, primary_key=True, nullable=False)
    eta = db.Column(db.Integer, nullable=False)
    condition = db.Column(db.String(64), nullable=False)
    current_location = db.Column(db.String(64), nullable=False)
    destination = db.Column(db.String(64), nullable=False)

    cat_id = db.Column(db.Integer, db.ForeignKey('cat.cat_id'), nullable=False)
    receiver_email = db.Column(db.String(64), db.ForeignKey('user.email'), nullable=False)

    __table_args__ = (db.ForeignKeyConstraint(['current_location', 'destination'], ['delivery_fee.current_location', 'delivery_fee.destination']),)

    @property
    def json(self):
        return {k: getattr(self, k).json if hasattr(getattr(self, k), 'json') else getattr(self, k) for k in [k for k in dir(self) if k[0] != '_' and k not in {'json', 'metadata', 'query', 'query_class'}]}

