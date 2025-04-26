import json
import os
from pathlib import Path

import sys
root_path=sys.path[1]
test_datapath="C:/Users/sivac/PycharmProjects/Python_SelRe/test_data/login/logindata.json"
print(test_datapath)


class JSON_Utility:
    @staticmethod
    def read_test_data(file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"No such file or directory: '{file_path}'")
        with open(test_datapath, 'r') as json_file:
            data = json.load(json_file)
        return data
    @staticmethod
    def load_test_data():
        with open(test_datapath, "r") as file:
            return json.load(file)["testdata_login"]


if __name__=="__main__":
    print(JSON_Utility.load_test_data())


