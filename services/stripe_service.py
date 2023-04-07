import stripe
from decouple import config
from werkzeug.exceptions import Unauthorized

stripe.api_key = config("STRIPE_SECRET_KEY")


class StripeService:
    STARTING_BALANCE = 20000
    ST_TO_LEV = 100

    @staticmethod
    def create_stripe_account(user):
        account = stripe.Customer.create(
            balance=StripeService.STARTING_BALANCE,
            name=f'{user["first_name"]} {user["last_name"]}',
            email=user['email'],
        )
        return account.id

    @staticmethod
    def purchase_ticket(ticket, user):
        customer = stripe.Customer.retrieve(user.stripe_account)

        if customer.balance < int(ticket.ticket_price * StripeService.ST_TO_LEV):
            raise Unauthorized("Insufficient funds")

        price = stripe.Price.create(
            unit_amount=int(ticket.ticket_price * StripeService.ST_TO_LEV),
            currency="bgn",
            product="ticket"
        )
        payment_intent = stripe.PaymentIntent.create(
            amount=price.unit_amount,
            currency=price.currency,
            customer=user.stripe_account,
            payment_method="pm_card_visa"
        )

        payment_intent.confirm()

        stripe.Customer.modify(
            user.stripe_account,
            balance=customer.balance - int(ticket.ticket_price * StripeService.ST_TO_LEV)
        )

        return payment_intent.id
