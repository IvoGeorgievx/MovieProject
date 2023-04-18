from models import User
from tests.base import TestRESTAPIBase


class TestRegistrationAndAuthorization(TestRESTAPIBase):
    def test_name_validator_upon_registration_expect_raise(self):
        headers = {"Content-Type": "application/json"}
        data = {
            "username": "Arditi9",
            "password": "12356",
            "first_name": "Ivo1",
            "last_name": "Georgiev1",
            "email": "b1334@a.bg",
            "stripe_account": ""
        }

        response = self.client.post('/register', json=data, headers=headers)
        assert response.status_code == 400
        assert response.json == {'message': {'first_name': ['Name must contain only alphabetic characters'],
                                             'last_name': ['Name must contain only alphabetic characters']}}

    def test_registration_with_valid_data_expect_success(self):
        headers = {"Content-Type": "application/json"}
        data = {
            "username": "Arditi9",
            "password": "12356",
            "first_name": "Ivo",
            "last_name": "Georgiev",
            "email": "b1334@a.bg",
            "stripe_account": ""
        }

        response = self.client.post('/register', json=data, headers=headers)
        assert response.status_code == 201
        user = User.query.all()
        assert len(user) == 1

    def test_registration_with_invalid_email_expect_raise(self):
        headers = {"Content-Type": "application/json"}
        data = {
            "username": "Arditi9",
            "password": "12356",
            "first_name": "Ivo",
            "last_name": "Georgiev",
            "email": "b@a.bg",
            "stripe_account": ""
        }
        response = self.client.post('/register', json=data, headers=headers)
        assert response.status_code == 400
        assert response.json == {'message': {'email': ['Invalid email address']}}

    def test_unique_email_and_username_validator_expect_raise(self):
        headers = {"Content-Type": "application/json"}
        data = {
            "username": "Arditi9",
            "password": "12356",
            "first_name": "Ivo",
            "last_name": "Georgiev",
            "email": "b1334@a.bg",
            "stripe_account": ""
        }
        response = self.client.post('/register', json=data, headers=headers)
        assert response.status_code == 201
        data = {
            "username": "Arditi9",
            "password": "12356",
            "first_name": "Ivo",
            "last_name": "Georgiev",
            "email": "b1334@a.bg",
            "stripe_account": ""
        }
        response = self.client.post('/register', json=data, headers=headers)
        assert response.status_code == 400
        assert response.json == {'message': {'email': ['Email already exists.'],
                                             'username': ['Username already exists']}}
        user = User.query.all()
        assert len(user) == 1

    def test_login_with_valid_credentials_expect_success(self):
        headers = {"Content-Type": "application/json"}
        data = {

            "username": "Arditi9",
            "password": "12356",
            "first_name": "Ivo",
            "last_name": "Georgiev",
            "email": "b1334@a.bg",
            "stripe_account": ""
        }
        response = self.client.post('/register', json=data, headers=headers)
        assert response.status_code == 201

        user = {
            "username": "Arditi9",
            "password": "12356"
        }

        response = self.client.post('/login', json=user, headers=headers)
        assert response.status_code == 200
