import time

from src.api.userservice import userservice_api

test = userservice_api()
token = test.get_valid_token()
print(f"Token: {token}")
print(f"Token age (seconds): {time.time() - test.token_expiry}")
# print(test.get_loggeinuser().to_json())

'''
import time
from datetime import datetime

def current_time_str():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


print(current_time_str())
# Convert strings to datetime objects
dt1 = datetime.strptime(current_time_str(), '%Y-%m-%d %H:%M:%S')
dt2 = datetime.strptime("2025-09-23 22:11:44", '%Y-%m-%d %H:%M:%S')

# Find the difference in seconds
diff_seconds = (dt2 - dt1).total_seconds()
print(f"Time difference in seconds: {diff_seconds}")
'''