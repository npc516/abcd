from flask import jsonify, request
from main import app, db
from model.cat import Cat
from model.comment import Comment
from model.auction import Auction

@app.route('/api/cats', methods=['GET'])
def all_cats():
    return jsonify([cat.json for cat in Cat.query.all()]), 200

@app.route('/api/cats/<id>', methods=['GET'])
def cat_get(id):
    return jsonify(Cat.query.get(id).json), 200

@app.route('/api/cats', methods=['POST'])
def create_cat():
    try:
        r = request.json
        cat = Cat(age=r['age'],
                  breed=r['breed'],
                  color=r['color'],
                  eye_color=r['eye_color'],
                  hometown=r['hometown'],
                  name=r['name'],
                  photo_path=r['photo_path'],
                  sex=r['sex'],
                  weight=r['weight'],
                  owner_email=r['owner_email'],
                  buy_it_now=r['buy_it_now']
                  )
        db.session.add(cat)
        db.session.commit()
    except Exception as e:
        print(e)
        return jsonify({'err': 'oops'}), 444
    return jsonify(cat.json), 201

@app.route('/api/cats/search', methods=['POST'])
def cat_search():
    try:
        r = request.json
        cats = Cat.query.filter()
        attrs = ['name', 'cat_id', 'color', 'breed', 'age', 'weight', 'eye_color', 'hometown', 'sex']
        for attr in attrs:
            if r[attr]:
                cats = cats.filter(getattr(Cat, attr) == r[attr])
        return jsonify([cat.json for cat in cats]), 200
    except RuntimeError as e:
        print(e)
        return jsonify({'err': 'oops'}), 444

@app.route('/api/cats/comments/<cat_id>', methods=['GET'])
def get_comments(cat_id):
    return jsonify([comment.json for comment in Comment.query.filter(Comment.cat_id == cat_id)]), 200

@app.route('/api/cats/auctions/<cat_id>', methods=['GET'])
def has_auction(cat_id):
    return jsonify([auction.json for auction in Auction.query.filter(Auction.cat_id == cat_id)]), 200
