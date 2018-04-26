from main import db

class Comment(db.Model):
    comment_id = db.Column(db.Integer, primary_key=True, nullable=False)
    content = db.Column(db.String(64), nullable=False)

    user_email = db.Column(db.String(64), db.ForeignKey('user.email'))
    cat_id = db.Column(db.Integer, db.ForeignKey('cat.cat_id'))

    @property
    def json(self):
        return {k: getattr(self, k).json if hasattr(getattr(self, k), 'json') else getattr(self, k) for k in [k for k in dir(self) if k[0] != '_' and k not in {'json', 'metadata', 'query', 'query_class'}]}
