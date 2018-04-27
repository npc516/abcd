from flask import jsonify, request
from main import app, db
from model.delivery import Delivery

@app.route('/api/delivery', methods=['POST'])
def create_delivery():
    try:
        r = request.json
        delivery = Delivery(
            eta=5,
            condition='Alive',
            current_location='State College',
            destination=r['destination'],
            cat_id=r['cat_id'],
            receiver_email=r['receiver_email'])
        db.session.add(delivery)
        db.session.commit()
        return jsonify(delivery.json), 201
    except Exception as e:
        print(e)
        return jsonify({'err': 'oops'}), 444
