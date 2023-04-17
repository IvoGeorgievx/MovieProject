from models import UserRole
from tests.base import TestRESTAPIBase, generate_token
from tests.user_factory import UserFactory


class TestLoginAndPermissionRequired(TestRESTAPIBase):

    def test_auth_is_required(self):
        all_guarded_urls = [
            ('POST', '/create-hall'),
            ('POST', '/create-movie'),
            ('POST', '/purchase-ticket'),
            ('GET', '/my-tickets'),
            ('PUT', '/update-movie/7'),
            ('DELETE', '/delete-movie/7')
        ]

        for method, url in all_guarded_urls:
            if method == 'GET':
                response = self.client.get(url)
            elif method == 'POST':
                response = self.client.post(url)
            elif method == 'PUT':
                response = self.client.put(url)
            else:
                response = self.client.delete(url)

            assert response.status_code == 401
            assert response.json == {"message": "Invalid or missing JWT token"}

    def test_permission_required(self):
        all_guarded_urls = [
            ('POST', '/create-movie'),
            ('PUT', '/update-movie/7'),
            ('POST', '/create-hall'),
        ]

        user = UserFactory(role=UserRole.regular)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}

        for method, url in all_guarded_urls:
            if method == 'GET':
                response = self.client.get(url, headers=headers)
            elif method == 'POST':
                response = self.client.post(url, headers=headers)
            elif method == 'PUT':
                response = self.client.put(url, headers=headers)
            else:
                response = self.client.delete(url, headers=headers)

            assert response.status_code == 403
            assert response.json == {"message": "You do not have permission to do that"}


