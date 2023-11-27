from flask import request
from flask_restful import Resource

from managers.auth import AuthManager
from schemas.request.users import UserRegisterSchemaIn, UserLoginSchema
from schemas.response.users import UserResponseSchema
from utilities.decorators import validate_schema


class Register(Resource):
    @validate_schema(UserRegisterSchemaIn)
    def post(self):
        data = request.get_json()
        user = AuthManager.register(data)
        token = AuthManager.encode_token(user)
        return UserResponseSchema().dump({"token": token}), 201


class Login(Resource):
    @validate_schema(UserLoginSchema)
    def post(self):
        data = request.get_json()
        user = AuthManager.login(data)
        token = AuthManager.encode_token(user)
        return UserResponseSchema().dump({"token": token}), 200
