from src.api.userservice import userservice_api

test= userservice_api()
print(test.get_loggeinuser().to_json())
