from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.ticket import TicketManager
from managers.transaction import TransactionManager
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
        TicketManager.check_for_available_tickets(data['movie_id'])
        ticket = TicketManager.create_ticket(data)
        payment = StripeService.purchase_ticket(ticket, current_user)
        if payment:
            TicketManager.confirm_payment(ticket)
            TransactionManager.create_transaction(ticket, payment, current_user)
            TicketManager.set_new_ticket_count(data['movie_id'])
        return {
            "ticket": TicketSchemaOut().dump(ticket),
            "barcode": payment
        }, 201


class UserTickets(Resource):
    @auth.login_required
    def get(self):
        user = auth.current_user()
        tickets = TicketManager.get_user_tickets(user)
        return {"tickets": TicketSchemaOut(many=True).dump(tickets)}, 200
