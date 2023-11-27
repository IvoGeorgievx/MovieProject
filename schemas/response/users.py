from marshmallow import Schema, fields


class UserResponseSchema(Schema):
    token = fields.String(required=True)
    user_id = fields.Integer(required=True)
