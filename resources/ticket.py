from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.ticket import TicketManager
from schemas.request.ticket import TicketSchemaIn
from schemas.response.ticket import TicketSchemaOut
from utilities.decorators import validate_schema


class Ticket(Resource):
    @auth.login_required
    @validate_schema(TicketSchemaIn)
    def get(self):
        data = request.get_json()
        current_user = auth.current_user()
        data['user_id'] = current_user.id
        ticket = TicketManager.create_ticket(data)
        return TicketSchemaOut().dump(ticket)
