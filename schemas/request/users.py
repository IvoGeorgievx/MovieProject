from marshmallow import fields, validate

from schemas.base_user import BaseUserSchema
from schemas.validators import UserValidator


class UserRegisterSchemaIn(BaseUserSchema):
    username = fields.String(required=True,
                             validate=validate.And(validate.Length(min=5, max=20), UserValidator.username_validator,
                                                   UserValidator.unique_username_validator))
    password = fields.String(required=True, validate=validate.Length(min=5))
    email = fields.String(required=True, validate=validate.And(UserValidator.email_validator,
                                                               UserValidator.unique_email_validator))
    first_name = fields.String(required=True,
                               validate=validate.And(validate.Length(min=3, max=20), UserValidator.name_validator))
    last_name = fields.String(required=True,
                              validate=validate.And(validate.Length(min=3, max=20), UserValidator.name_validator))
    stripe_account = fields.String(required=False)


class UserLoginSchema(BaseUserSchema):
    pass
