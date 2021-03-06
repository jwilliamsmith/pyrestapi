from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}
    
    @classmethod
    def find_by(cls, criteria):
        if criteria[0] == 'name':
            return cls.query.filter_by(name=criteria[1]).first()
        elif criteria[1] == 'id':
            return cls.query.filter_by(id=criteria[1]).first()               
        else:
            return None

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit() 