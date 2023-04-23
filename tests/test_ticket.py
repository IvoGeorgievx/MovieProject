from unittest.mock import patch

from managers.hall import HallManager
from models import UserRole, Transaction, Ticket, User
from services.stripe_service import StripeService
from tests.base import TestRESTAPIBase, generate_token
from tests.factories import UserFactory, normal_test_movie_data


class TestTicketSchemas(TestRESTAPIBase):
    @patch.object(StripeService, "purchase_ticket", return_value="some string 1 2 3 4")
    def test_purchase_ticket_expect_success_and_created_transaction(
        self, purchase_ticket
    ):
        transaction = Transaction.query.all()
        assert len(transaction) == 0

        user = UserFactory(role=UserRole.admin)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}
        hall = HallManager.create_hall({"capacity": 5})
        data = normal_test_movie_data(hall)
        response = self.client.post("/create-movie", json=data, headers=headers)
        assert response.status_code == 201

        user = UserFactory(role=UserRole.regular)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}
        data = {"movie_id": 1}

        response = self.client.post("/purchase-ticket", json=data, headers=headers)
        assert response.status_code == 201
        user = User.query.all()[1]
        assert response.json == {
            "barcode": "some string 1 2 3 4",
            "ticket": {
                "id": 1,
                "is_paid": True,
                "movie_id": 1,
                "ticket_price": 35.65,
                "user_id": user.id,
            },
        }

        transaction = Transaction.query.all()
        ticket = Ticket.query.all()[0]
        purchase_ticket.assert_called_once_with(ticket, user)
        assert len(transaction) == 1
        assert len(user.tickets) == 1

    def test_ticket_purchase_when_no_tickets_left_expect_raise(self):
        user = UserFactory(role=UserRole.admin)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}
        hall = HallManager.create_hall({"capacity": 0})
        data = normal_test_movie_data(hall)
        response = self.client.post("/create-movie", json=data, headers=headers)
        assert response.status_code == 201

        user = UserFactory(role=UserRole.regular)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}
        data = {"movie_id": 1}
        response = self.client.post("/purchase-ticket", json=data, headers=headers)
        assert response.status_code == 400
        assert response.json == {"message": "Tickets are all sold out."}
        transaction = Transaction.query.all()
        ticket = Ticket.query.all()
        assert len(transaction) == 0
        assert len(ticket) == 0

    @patch.object(StripeService, "purchase_ticket", return_value="some string 1 2 3 4")
    def test_ticket_manager_confirm_payment_expect_success(self, purchase_ticket):
        transaction = Transaction.query.all()
        assert len(transaction) == 0

        user = UserFactory(role=UserRole.admin)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}
        hall = HallManager.create_hall({"capacity": 5})
        data = normal_test_movie_data(hall)

        self.client.post("/create-movie", json=data, headers=headers)

        user = UserFactory(role=UserRole.regular)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}
        data = {"movie_id": 1}

        self.client.post("/purchase-ticket", json=data, headers=headers)

        ticket = Ticket.query.all()[0]
        purchase_ticket.assert_called_once_with(ticket, user)
        assert ticket.is_paid
