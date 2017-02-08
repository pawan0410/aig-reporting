from emr.extensions import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean, default=False)
    authenticated = db.Column(db.Boolean, default=False)

    def get_id(self):
        return self.id

    def is_active(self):
        return self.active

    def is_authenticated(self):
        return self.authenticated

