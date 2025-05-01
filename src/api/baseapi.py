import requests
import json
import os

from fwutilities.readconfig_utiltiy import Read_Config
from src.api import configapi


class Base_api:
    def __init__(self):
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        self.headers_with_basic_auth = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"{self.oauth_access(Read_Config.get_username(), Read_Config.get_password())}"
        }

    @staticmethod
    def oauth_access(username, password):
        payload = json.dumps({
            "email": username,
            "password": password
        })
        headers = {
            'Content-Type': 'application/json',
        }
        url=configapi.BASE_URI+configapi.LOG_IN
        response = requests.post(url, headers=headers, data=payload)
        token= response.json().get("token")
        return f"Bearer {token}"

