from datetime import datetime, timedelta

import jwt
from decouple import config
from flask_httpauth import HTTPTokenAuth
from werkzeug.exceptions import BadRequest, Unauthorized
from werkzeug.security import generate_password_hash, check_password_hash

from db import db
from models import User
from services.stripe_service import StripeService


class AuthManager:

    @staticmethod
    def register(data):
        data['password'] = generate_password_hash(data['password'], method='sha256')
        if not data['stripe_account']:
            data['stripe_account'] = StripeService.create_stripe_account(data)
        user = User(**data)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def login(data):
        user = User.query.filter_by(username=data['username']).first()
        if not user:
            raise Unauthorized("Invalid username or password")
        if not check_password_hash(user.password, data['password']):
            raise Unauthorized("Invalid username or password")
        return user

    @staticmethod
    def encode_token(user):
        payload = {
            'sub': user.id,
            'exp': datetime.utcnow() + timedelta(days=15)
        }
        return jwt.encode(payload, key=config("JWT_SECRET_KEY"), algorithm='HS256')

    @staticmethod
    def decode_token(token):
        try:
            return jwt.decode(token, key=config("JWT_SECRET_KEY"), algorithms=['HS256'])
        except Exception as ex:
            raise BadRequest("Invalid or missing JWT token")


auth = HTTPTokenAuth(scheme='Bearer')


@auth.verify_token
def verify_token(token):
    try:
        payload = AuthManager.decode_token(token)
        user = User.query.filter_by(id=payload['sub']).first()
        if not user:
            raise Unauthorized("Invalid or missing JWT token")
        return user
    except Exception as ex:
        raise BadRequest("Invalid or missing JWT token")
