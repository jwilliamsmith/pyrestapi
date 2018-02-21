import sqlite3
from models.user import UserModel
from flask_restful import Resource, reqparse

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="Username cannot be blank.")
    parser.add_argument('password', type=str, required=True, help="Password cannot be blank.")
    def post(self):
        data = UserRegister.parser.parse_args()
        criteria = (data['username'], data['password'])
        if UserModel.find_by(('username', criteria[0])):
            return {"message": "A user with that username exists."}, 400

        user = UserModel(**data)
        user.save()
        
        return {"message": "User created."}, 201
