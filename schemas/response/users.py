from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Integer()
    username = fields.String(required=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.String(required=True)


class UserResponseSchema(Schema):
    token = fields.String(required=True)
    user = fields.Nested(UserSchema)
