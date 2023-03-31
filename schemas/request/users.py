from marshmallow import fields

from schemas.base_user import BaseUserSchema


class UserRegisterSchemaIn(BaseUserSchema):

    email = fields.String(required=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    card_number = fields.Integer(required=True)


class UserLoginSchema(BaseUserSchema):
    pass


# TODO: add validators
