from main import db

class Cat(db.Model):
    cat_id = db.Column(db.Integer, primary_key=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    breed = db.Column(db.String(64), nullable=False)
    color = db.Column(db.String(64), nullable=False)
    eye_color = db.Column(db.String(64), nullable=False)
    hometown = db.Column(db.String(64), nullable=False)
    name = db.Column(db.String(64), nullable=False)
    photo_path = db.Column(db.String(64), nullable=False)
    sex = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    buy_it_now = db.Column(db.Integer, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    insurer_crn = db.Column(db.String(64), nullable=True)
    sponsor_crn = db.Column(db.String(64), nullable=True)
    policy_id = db.Column(db.Integer, nullable=True)
    sponsorship_id = db.Column(db.Integer, nullable=True)

    trainer_ssn = db.Column(db.String(64), db.ForeignKey('trainer.ssn'), nullable=True)
    owner_email = db.Column(db.String(64), db.ForeignKey('user.email'), nullable=False)
    audition_id = db.Column(db.Integer, db.ForeignKey('audition.event_id'), nullable=True)

    __table_args__ = (db.ForeignKeyConstraint(['insurer_crn', 'policy_id'], ['policy.crn', 'policy.policy_id']),
                     db.ForeignKeyConstraint(['sponsor_crn', 'sponsorship_id'], ['sponsorship.crn', 'sponsorship.sponsorship_id']),)
    
    @property
    def json(self):
        return {k: getattr(self, k).json if hasattr(getattr(self, k), 'json') else getattr(self, k) for k in [k for k in dir(self) if k[0] != '_' and k not in {'json', 'metadata', 'query', 'query_class'}]}
