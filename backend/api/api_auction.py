from flask import jsonify, request
from main import app, db
from model.auction import Auction

@app.route('/api/auctions', methods=['POST'])
def create_auction():
    try:
        r = request.json
        auction = Auction(start_time=r['start_time'],
                          start_price=r['start_price'],
                          duration=r['duration'],
                          bid_increment=r['bid_increment'],
                          cat_id=r['cat_id'])
        db.session.add(auction)
        db.session.commit()
    except Exception as e:
        print(e)
        return jsonify({'err': 'oops'}), 444
    return jsonify(auction.json), 201
