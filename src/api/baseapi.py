import time

import requests
import json
import os

from fwutilities.readconfig_utiltiy import Read_Config
from src.api import configapi


class Base_api:
    token = None
    token_expiry = 0  # Store token expiration time (in seconds since epoch)
    token_file = "token_cache.json"

    def __init__(self):
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        self.load_token()

    def load_token(self):
        if os.path.exists(self.token_file):
            with open(self.token_file, "r") as f:
                data = json.load(f)
                Base_api.token = data.get("token")
                Base_api.token_expiry = data.get("token_expiry", 0)

    def save_token(self):
        with open(self.token_file, "w") as f:
            json.dump({"token": Base_api.token, "token_expiry": Base_api.token_expiry}, f)

    def get_valid_token(self):
        # Only generate a new token if the previous one is older than 5 hours (18000 seconds)
        if Base_api.token and (time.time() - Base_api.token_expiry) <= 18000:
            return f"Bearer {Base_api.token}"
        # Otherwise, generate a new token
        Base_api.token, Base_api.token_expiry = self.oauth_access(Read_Config.get_username(), Read_Config.get_password())
        self.save_token()
        return f"Bearer {Base_api.token}"

    @staticmethod
    def oauth_access(username, password):
        payload = json.dumps({
            "email": username,
            "password": password
        })
        headers = {
            'Content-Type': 'application/json',
        }
        url = configapi.BASE_URI + configapi.LOG_IN
        response = requests.post(url, headers=headers, data=payload)
        response_data = response.json()
        token = response_data.get("token")
        # Store the token generation time
        token_expiry = time.time()
        return token, token_expiry

    def get_headers_with_basic_auth(self):
        return {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": self.get_valid_token()
        }