from flask import jsonify, request
from main import app, db
from model.auction import Auction
from model.cat import Cat

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

@app.route('/api/buyitnow', methods=['POST'])
def delete_auction():
    cat_id = request.json['cat_id']
    db.session.query(Auction).filter(Auction.cat_id == cat_id).delete()
    cat = Cat.query.get(cat_id)
    cat.buy_it_now = None
    db.session.commit()
    return jsonify({'status': 'success'}), 200
