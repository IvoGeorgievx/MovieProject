from marshmallow import Schema, fields


class UserResponseSchema(Schema):
    token = fields.String(required=True)