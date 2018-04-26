from main import db

class Auction(db.Model):
    auction_id = db.Column(db.Integer, primary_key=True, nullable=False)
    start_time = db.Column(db.Integer, nullable=False)
    start_price = db.Column(db.Integer, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    bid_increment = db.Column(db.Integer, nullable=False)

    cat_id = db.Column(db.Integer, db.ForeignKey('cat.cat_id'), nullable=False)

    bid = db.relationship('Bid', backref='auction')

    @property
    def json(self):
        return {k: getattr(self, k) for k in dir(self) if k[0] != '_' and k not in {'json', 'metadata', 'query', 'query_class'}}
