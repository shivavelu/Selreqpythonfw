from fwutilities.apiservices import APIRequest
from src.api.baseapi import Base_api
from src.api.configapi import BASE_URI, USER_LOGIN


class userservice_api(Base_api):
    def __init__(self):
        super().__init__()
        self.base_url = BASE_URI
        self.request = APIRequest()

    def get_loggeinuser(self):
        url = f"{BASE_URI}/{USER_LOGIN}"
        return self.request.get_request(url, self.headers_with_basic_auth)

