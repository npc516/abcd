from flask import jsonify, request
from main import app, db
from model.user import User
from model.cat import Cat

@app.route('/api/users', methods=['POST'])
def user_create():
    try:
        user = User(email=request.json['email'],
                    name=request.json['name'],
                    password=request.json['password'],
                    bank_account=request.json['bank_account'],
                    phone=int(request.json['phone']),
                    address=request.json['address'])
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        return jsonify({'err': 'oops'}), 444
    return jsonify(user.json), 200

@app.route('/api/users/<email>', methods=['POST'])
def user_login(email):
    if request.json['password'] == User.query.get(email).password:
        return jsonify(User.query.get(email).json), 200
    else:
        return jsonify({'err': 'oops'}), 444

@app.route('/api/users/cats/<email>', methods=['GET'])
def user_cats(email):
    return jsonify([cat.json for cat in Cat.query.filter(Cat.owner_email == email)]), 200
