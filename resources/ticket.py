from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.ticket import TicketManager
from schemas.request.ticket import TicketSchemaIn
from schemas.response.ticket import TicketSchemaOut
from services.stripe_service import StripeService
from utilities.decorators import validate_schema


class TicketPurchase(Resource):
    @auth.login_required
    @validate_schema(TicketSchemaIn)
    def post(self):
        data = request.get_json()
        current_user = auth.current_user()
        data['user_id'] = current_user.id
        data['ticket_price'] = TicketManager.set_ticket_price(data['movie_id'])
        ticket = TicketManager.create_ticket(data)
        purchase_ticket = StripeService.purchase_ticket(ticket, current_user)
        if purchase_ticket:
            TicketManager.confirm_payment(ticket)
        return {
            "ticket": TicketSchemaOut().dump(ticket),
            "barcode": purchase_ticket
        }


class UserTickets(Resource):
    @auth.login_required
    def get(self):
        user = auth.current_user()
        tickets = TicketManager.get_user_tickets(user)
        return {"tickets": TicketSchemaOut(many=True).dump(tickets)}
