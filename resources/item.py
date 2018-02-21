from flask_jwt import JWT, jwt_required
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="Price cannot be blank.")
    parser.add_argument('store_id', type=int, required=True, help="Every item needs a store id.")

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by(('name', name))
        if item:
            return item.json()
        return {'message': 'Item not found.'}

    def post(self, name):
        if ItemModel.find_by(('name',name)):
            return {"error": "An item named {} already exists".format(name)}, 400
        data = Item.parser.parse_args()
        item = ItemModel(name, **data)
        print(item.json())
        try:
            item.save()
        except:
            return {'error': 'Item was not created.'}, 500
        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by(('name', name))
        if item:
            item.delete()
        return {'message': '{} deleted'.format(name)}

    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by(('name', name))
        if item:
            item.price = data['price']
        else:
            item = ItemModel(name, **data)
        item.save()
        return item.json(), 201

class ItemList(Resource):
    def get(self):
        print(ItemModel.query.all())
        return {'items':  [item.json() for item in ItemModel.query.all()]}
