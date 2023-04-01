from marshmallow import fields, validate

from schemas.base_user import BaseUserSchema
from schemas.validators import name_validator


class UserRegisterSchemaIn(BaseUserSchema):
    email = fields.String(required=True)
    first_name = fields.String(required=True,
                               validate=validate.And(validate.Length(min=3, max=20), name_validator))
    last_name = fields.String(required=True,
                              validate=validate.And(validate.Length(min=3, max=20), name_validator))
    card_number = fields.Integer(required=True)
    # TODO: add validator for card_number


class UserLoginSchema(BaseUserSchema):
    pass

# TODO: add validators
