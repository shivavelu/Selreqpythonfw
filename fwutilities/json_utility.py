import json
import os


class Utility:
    @staticmethod
    def read_test_data(file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"No such file or directory: '{file_path}'")
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        return data


read=Utility.read_test_data("C:/Users/sivac/PycharmProjects/Python_SelRe/test_data/login/logindata.json")
print(read)