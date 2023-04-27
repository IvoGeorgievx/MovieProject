from unittest.mock import patch

from managers.hall import HallManager
from models import UserRole, Movie, Ticket
from services.stripe_service import StripeService
from services.tmdb import TMDBService
from tests.base import TestRESTAPIBase, generate_token
from tests.factories import UserFactory


class TestMovieSchema(TestRESTAPIBase):
    def test_browse_all_movies_expect_success(self):
        movies = Movie.query.all()
        assert len(movies) == 0

        user = UserFactory(role=UserRole.admin)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}
        hall = HallManager.create_hall({"capacity": 5})
        data = {
            "name": "Test Movie1",
            "rating": 10,
            "description": "one of the best movies",
            "hall_id": hall.id,
            "ticket_price": 35.65,
            "start_time": "2023-04-17T21:31:00.000000",
            "end_time": "2023-04-17T22:30:00.000000",
        }
        response = self.client.post("/create-movie", json=data, headers=headers)
        assert response.status_code == 201

        response = self.client.get("/browse-movies")
        assert response.status_code == 200
        assert response.json == [
            {
                "description": "one of the best movies",
                "end_time": "2023-04-17T22:30:00",
                "hall_id": 1,
                "id": 1,
                "name": "Test Movie1",
                "rating": 10.0,
                "start_time": "2023-04-17T21:31:00",
                "ticket_price": 35.65,
            }
        ]

    def test_create_movie_with_missing_required_fields_expect_raises(self):
        user = UserFactory(role=UserRole.admin)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}

        data = {}

        response = self.client.post("/create-movie", json=data, headers=headers)

        assert response.status_code == 400
        assert response.json == {
            "message": {
                "description": ["Missing data for required field."],
                "end_time": ["Missing data for required field."],
                "hall_id": ["Missing data for required field."],
                "name": ["Missing data for required field."],
                "rating": ["Missing data for required field."],
                "start_time": ["Missing data for required field."],
                "ticket_price": ["Missing data for required field."],
            }
        }

    def test_create_movie_with_valid_fields_expect_creation(self):
        user = UserFactory(role=UserRole.admin)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}
        hall = HallManager.create_hall({"capacity": 5})
        data = {
            "name": "Test Movie",
            "rating": 5.0,
            "description": "one of the best movies",
            "hall_id": hall.id,
            "ticket_price": 35.65,
            "start_time": "2023-04-17T21:31:00.000000",
            "end_time": "2023-04-17T22:30:00.000000",
        }

        response = self.client.post("/create-movie", json=data, headers=headers)
        assert response.status_code == 201
        assert response.json == {
            "description": "one of the best movies",
            "end_time": "2023-04-17T22:30:00",
            "hall_id": hall.id,
            "id": 1,
            "name": "Test Movie",
            "rating": 5.0,
            "start_time": "2023-04-17T21:31:00",
            "ticket_price": 35.65,
        }

    def test_create_movie_with_invalid_rating_expect_raise(self):
        user = UserFactory(role=UserRole.admin)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}
        hall = HallManager.create_hall({"capacity": 5})
        data = {
            "name": "Test Movie",
            "rating": 10.1,
            "description": "one of the best movies",
            "hall_id": hall.id,
            "ticket_price": 35.65,
            "start_time": "2023-04-17T21:31:00.000000",
            "end_time": "2023-04-17T22:30:00.000000",
        }

        response = self.client.post("/create-movie", json=data, headers=headers)
        assert response.status_code == 400
        assert response.json == {
            "message": {"rating": ["Movie ratings must be between 0 and 10 inclusive"]}
        }

    def test_create_movie_that_interferes_with_another_movie_expect_raise(self):
        user = UserFactory(role=UserRole.admin)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}
        hall = HallManager.create_hall({"capacity": 5})
        data = {
            "name": "Test Movie1",
            "rating": 10,
            "description": "one of the best movies",
            "hall_id": hall.id,
            "ticket_price": 35.65,
            "start_time": "2023-04-17T21:31:00.000000",
            "end_time": "2023-04-17T22:30:00.000000",
        }

        response = self.client.post("/create-movie", json=data, headers=headers)
        assert response.status_code == 201
        data = {
            "name": "Test Movie2",
            "rating": 10,
            "description": "one of the best movies",
            "hall_id": hall.id,
            "ticket_price": 35.65,
            "start_time": "2023-04-17T21:31:00.000000",
            "end_time": "2023-04-17T22:30:00.000000",
        }
        response = self.client.post("/create-movie", json=data, headers=headers)
        assert response.status_code == 400
        assert response.json == {
            "message": "Hall is occupied during that time.Set another timeframe or choose "
            "other hall."
        }

    def test_create_movie_with_same_screening_time_but_different_hall_expect_success(
        self,
    ):
        user = UserFactory(role=UserRole.admin)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}
        first_hall = HallManager.create_hall({"capacity": 5})
        data = {
            "name": "Test Movie1",
            "rating": 10,
            "description": "one of the best movies",
            "hall_id": first_hall.id,
            "ticket_price": 35.65,
            "start_time": "2023-04-17T21:31:00.000000",
            "end_time": "2023-04-17T22:30:00.000000",
        }
        response = self.client.post("/create-movie", json=data, headers=headers)
        assert response.status_code == 201

        second_hall = HallManager.create_hall({"capacity": 10})
        data = {
            "name": "Test Movie2",
            "rating": 10,
            "description": "one of the best movies",
            "hall_id": second_hall.id,
            "ticket_price": 35.65,
            "start_time": "2023-04-17T21:31:00.000000",
            "end_time": "2023-04-17T22:30:00.000000",
        }

        response = self.client.post("/create-movie", json=data, headers=headers)
        assert response.status_code == 201

    def test_create_movie_with_non_existing_hall_expect_raise(self):
        user = UserFactory(role=UserRole.admin)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}
        data = {
            "name": "Test Movie1",
            "rating": 10,
            "description": "one of the best movies",
            "hall_id": 5,
            "ticket_price": 35.65,
            "start_time": "2023-04-17T21:31:00.000000",
            "end_time": "2023-04-17T22:30:00.000000",
        }
        response = self.client.post("/create-movie", json=data, headers=headers)
        assert response.status_code == 400
        assert response.json == {
            "message": {"hall_id": ["Hall with that ID does not exist."]}
        }

    def test_create_movie_with_invalid_ticket_price_expect_raise(self):
        user = UserFactory(role=UserRole.admin)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}
        hall = HallManager.create_hall({"capacity": 5})
        data = {
            "name": "Test Movie1",
            "rating": 10,
            "description": "one of the best movies",
            "hall_id": hall.id,
            "ticket_price": -5,
            "start_time": "2023-04-17T21:31:00.000000",
            "end_time": "2023-04-17T22:30:00.000000",
        }
        response = self.client.post("/create-movie", json=data, headers=headers)
        assert response.status_code == 400
        assert response.json == {
            "message": {"ticket_price": ["Ticket price must be higher than 0."]}
        }

    def test_delete_movie_expect_success(self):
        user = UserFactory(role=UserRole.admin)
        token = generate_token(user)
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }
        first_hall = HallManager.create_hall({"capacity": 5})
        data = {
            "name": "Test Movie1",
            "rating": 10,
            "description": "one of the best movies",
            "hall_id": first_hall.id,
            "ticket_price": 35.65,
            "start_time": "2023-04-17T21:31:00.000000",
            "end_time": "2023-04-17T22:30:00.000000",
        }
        self.client.post("/create-movie", json=data, headers=headers)
        movie = Movie.query.all()
        assert len(movie) == 1
        response = self.client.delete("/movie/1", json={}, headers=headers)
        assert response.status_code == 204
        movie = Movie.query.all()
        assert len(movie) == 0

    def test_delete_movie_with_wrong_id_expect_404(self):
        user = UserFactory(role=UserRole.admin)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}
        first_hall = HallManager.create_hall({"capacity": 5})
        data = {
            "name": "Test Movie1",
            "rating": 10,
            "description": "one of the best movies",
            "hall_id": first_hall.id,
            "ticket_price": 35.65,
            "start_time": "2023-04-17T21:31:00.000000",
            "end_time": "2023-04-17T22:30:00.000000",
        }
        self.client.post("/create-movie", json=data, headers=headers)
        response = self.client.delete("/movie/2", json={}, headers=headers)
        assert response.status_code == 404
        movie = Movie.query.all()
        assert len(movie) == 1

    def test_update_movie_with_invalid_data_expect_raise(self):
        user = UserFactory(role=UserRole.admin)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}
        hall = HallManager.create_hall({"capacity": 5})
        data = {
            "name": "Test Movie1",
            "rating": 10,
            "description": "one of the best movies",
            "hall_id": hall.id,
            "ticket_price": 12.50,
            "start_time": "2023-04-17T21:31:00.000000",
            "end_time": "2023-04-17T22:30:00.000000",
        }
        response = self.client.post("/create-movie", json=data, headers=headers)
        assert response.status_code == 201

        data = {
            "name": "Test Movie1",
            "rating": 11,
            "description": "one of the best movies",
            "hall_id": hall.id,
            "ticket_price": 0,
            "start_time": "2023-04-17T21:31:00.000000",
            "end_time": "2023-04-17T22:30:00.000000",
        }

        response = self.client.put("/movie/1", json=data, headers=headers)
        assert response.status_code == 400
        assert response.json == {
            "message": {
                "rating": ["Movie ratings must be between 0 and 10 inclusive"],
                "ticket_price": ["Ticket price must be higher than 0."],
            }
        }

    def test_update_movie_with_correct_data_expect_success(self):
        user = UserFactory(role=UserRole.admin)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}
        hall = HallManager.create_hall({"capacity": 5})
        data = {
            "name": "Test Movie1",
            "rating": 10,
            "description": "one of the best movies",
            "hall_id": hall.id,
            "ticket_price": 12.50,
            "start_time": "2023-04-17T21:31:00.000000",
            "end_time": "2023-04-17T22:30:00.000000",
        }
        response = self.client.post("/create-movie", json=data, headers=headers)
        assert response.status_code == 201

        data = {
            "name": "Test Movie1",
            "rating": 6,
            "description": "one of the best movies",
            "hall_id": hall.id,
            "ticket_price": 12.50,
            "start_time": "2023-04-17T21:31:00.000000",
            "end_time": "2023-04-17T22:30:00.000000",
        }
        response = self.client.put("/movie/1", json=data, headers=headers)
        assert response.status_code == 200
        assert response.json == {
            "description": "one of the best movies",
            "end_time": "2023-04-17T22:30:00",
            "hall_id": hall.id,
            "id": 1,
            "name": "Test Movie1",
            "rating": 6.0,
            "start_time": "2023-04-17T21:31:00",
            "ticket_price": 12.5,
        }

    @patch.object(TMDBService, "get_movie_id", return_value="157336")
    @patch.object(
        TMDBService,
        "get_movie_details",
        return_value={
            "overview": "The adventures of a group of explorers who make use of a newly discovered wormhole...",
            "budget": 1500000,
            "genres": [{"name": "Adventure"}],
        },
    )
    def test_get_movie_details_expect_success(
        self, mock_get_movie_details, mock_get_movie_id
    ):
        response = self.client.get("/search-movie/Interstellar")
        assert response.status_code == 200
        mock_get_movie_id.assert_called_once_with("Interstellar")
        mock_get_movie_details.assert_called_once_with("157336")
        assert response.json == {
            "overview": "The adventures of a group of explorers who make use of a newly discovered wormhole...",
            "budget": 1500000,
            "genres": [{"name": "Adventure"}],
        }

    @patch.object(
        TMDBService,
        "get_upcoming_movies",
        return_value={
            "results": [
                {
                    "original_title": "test_upcoming_movie",
                    "release_date": "test_date",
                    "overview": "test description",
                }
            ]
        },
    )
    def test_get_upcoming_movies_expect_success(self, mock_get_upcoming_movies):
        response = self.client.get("/upcoming-movies")
        assert response.status_code == 200
        mock_get_upcoming_movies.assert_called_once_with()
        assert response.json == {
            "results": [
                {
                    "original_title": "test_upcoming_movie",
                    "release_date": "test_date",
                    "overview": "test description",
                }
            ]
        }

    @patch.object(StripeService, "purchase_ticket", return_value="123456")
    def test_delete_movie_with_tickets_and_transactions_expect_success(
        self, mock_purchase_ticket
    ):
        user = UserFactory(role=UserRole.admin)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}
        hall = HallManager.create_hall({"capacity": 5})
        data = {
            "name": "Test Movie",
            "rating": 5.0,
            "description": "one of the best movies",
            "hall_id": hall.id,
            "ticket_price": 35.65,
            "start_time": "2023-04-17T21:31:00.000000",
            "end_time": "2023-04-17T22:30:00.000000",
        }
        response = self.client.post("/create-movie", json=data, headers=headers)
        assert response.status_code == 201
        movie = Movie.query.all()[0]
        data = {"movie_id": movie.id}

        response = self.client.post("/purchase-ticket", json=data, headers=headers)
        ticket = Ticket.query.all()[0]
        mock_purchase_ticket.assert_called_once_with(ticket, user)
        assert response.status_code == 201
        assert response.json == {
            "barcode": "123456",
            "ticket": {
                "id": 1,
                "is_paid": True,
                "movie_id": 1,
                "ticket_price": 35.65,
                "user_id": user.id,
            },
        }
