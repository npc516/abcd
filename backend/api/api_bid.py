from flask import jsonify, request
from main import app, db
from model.bid import Bid
from model.auction import Auction

@app.route('/api/bids/<cat_id>', methods=['GET'])
def get_high_bid(cat_id):
    auction = Auction.query.filter(Auction.cat_id == cat_id)[0]
    bids = Bid.query.filter(Bid.auction_id == auction.auction_id).all()
    if not bids:
        return jsonify({'price': 0}), 200
    max_bid = max(bids, key=lambda b:b.price)
    return jsonify(max_bid.json), 200

@app.route('/api/bids', methods=['POST'])
def create_bid():
    try:
        r = request.json
        auction = Auction.query.filter(Auction.cat_id == r['cat_id'])[0]
        bid = Bid(price=r['price'],
                  user_email=r['user_email'],
                  auction_id=auction.auction_id)
        db.session.add(bid)
        db.session.commit()
        return jsonify(bid.json), 200
    except Exception as e:
        print(e)
        return jsonify({'err': 'oops'}), 444
