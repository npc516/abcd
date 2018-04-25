from flask import jsonify, request
from main import app, db
from model.cat import Cat

@app.route('/api/cats', methods=['GET'])
def all_cats():
    return jsonify([cat.json for cat in Cat.query.all()]), 200

@app.route('/api/cats/<id>', methods=['GET'])
def cat_get(id):
    return Cat.query.get(id)

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
                  owner_email=r['owner_email']
                  )
        db.session.add(cat)
        db.session.commit()
    except Exception as e:
        return jsonify({'err': 'oops'}), 444
    return jsonify(cat.json), 201
