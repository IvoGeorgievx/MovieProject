from marshmallow import fields

from schemas.base_hall import BaseHallSchema


class HallSchemaOut(BaseHallSchema):
    id = fields.Integer(required=True)

