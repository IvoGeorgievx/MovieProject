from marshmallow import fields

from schemas.base_ticket import BaseTicketSchema


class TicketSchemaOut(BaseTicketSchema):
    user_id = fields.Integer(required=True)
    id = fields.Integer(required=True)
