from marshmallow import Schema, fields


class BaseUserSchema(Schema):

    username = fields.String(required=True)
    password = fields.String(required=True)


