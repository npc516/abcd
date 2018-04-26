from main import db

class Bid(db.Model):
    bid_id = db.Column(db.Integer, primary_key=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)

    user_email = db.Column(db.String(64), db.ForeignKey('user.email'), nullable=False)
    auction_id = db.Column(db.Integer, db.ForeignKey('auction.auction_id'), nullable=False)

    @property
    def json(self):
        return {k: getattr(self, k).json if hasattr(getattr(self, k), 'json') else getattr(self, k) for k in [k for k in dir(self) if k[0] != '_' and k not in {'json', 'metadata', 'query', 'query_class'}]}
