import os
import requests
from dotenv import load_dotenv

load_dotenv()

class ApiClient:
    def __init__(self):
        self.base_url = os.getenv("API_URL")
        self.session = requests.Session()

    def get(self, endpoint, params=None):
        response = self.session.get(f'{self.base_url}/{endpoint}', params=params)
        return response

    def post(self, endpoint, data):
        response = self.session.post(f'{self.base_url}/{endpoint}', json=data)
        return response

    def put(self, endpoint, data):
        response = self.session.put(f'{self.base_url}/{endpoint}', json=data)
        return response

    def delete(self, endpoint, data):
        response = self.session.delete(f'{self.base_url}/{endpoint}', json=data)
        return response