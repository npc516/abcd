from flask import jsonify, request
from main import app, db
from model.comment import Comment

@app.route('/api/comments', methods=['POST'])
def create_comment():
	try:
		r = request.json
		comment = Comment(
			content=r['content'],
			user_email=r['user_email'],
			cat_id=r['cat_id'])
		db.session.add(comment)
		db.session.commit()
	except Exception as e:
		print(e)
		return jsonify({'err': 'oops'}), 444
	return jsonify(comment.json), 201