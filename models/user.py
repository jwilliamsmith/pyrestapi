import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by(cls, criteria):
        if criteria[0] == 'username':
            return cls.query.filter_by(username=criteria[1]).first()
        elif criteria[0] == 'id':
            return cls.query.filter_by(id=criteria[1]).first()
        return None