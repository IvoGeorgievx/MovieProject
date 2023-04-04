import uuid

import requests
from decouple import config


class WiseService:
    def __init__(self):
        self.url = 'https://api.sandbox.transferwise.tech/'
        self.headers = {
            'Authorization': f'Bearer {config("WISE_KEY")}',
            'Content-Type': 'application/json'
        }
        self.recipient_account_id = 16693349

    def get_business_account_id(self):
        url = self.url + f'/v1/profiles/{self.recipient_account_id}'
        response = requests.get(url, json={}, headers=self.headers)
        return response.json()

    def generate_client_credentials_token(self):
        url = self.url + f'oauth/token'
        response = requests.post(url, json={}, headers='')
        return response

    def create_user_account(self, user):
        url = self.url + f'v1/user/signup/registration_code'
        body = {
            "email": user.email,
            "registrationCode": f'{str(uuid.uuid4())}',
            "language": "EN"
        }
        response = requests.post(url, json=body, headers=self.headers)
        return response.json()


# if __name__ == '__main__':
#     wise = WiseService()
#     print(wise.generate_client_credentials_token())
