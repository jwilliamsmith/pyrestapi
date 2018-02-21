from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by(('name', name))
        if store:
            return store.json()
        return {'message': 'Store not found.'}, 404
    
    def post(self, name):
        if StoreModel.find_by(('name', name)):
            return {'message': 'A Store named {} already exists.'.format(name)}
        store = StoreModel(name)
        try: 
            store.save()
        except:
            return {'message': 'An error occurred'}, 500
        return store.json()

    def delete(self, name):
        store = StoreModel.find(name)
        if store:
            store.delete()
        return {'message': 'Store deleted.'}

    
class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}