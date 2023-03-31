from flask import request
from flask_restful import Resource

from managers.auth import AuthManager
from schemas.response.users import UserResponseSchema


class Register(Resource):
    def post(self):
        data = request.get_json()
        user = AuthManager.register(data)
        token = AuthManager.encode_token(user)
        return UserResponseSchema().dump({"token": token})


class Login(Resource):
    def post(self):
        data = request.get_json()
        user = AuthManager.login(data)
        token = AuthManager.encode_token(user)
        return UserResponseSchema().dump({"token": token})
