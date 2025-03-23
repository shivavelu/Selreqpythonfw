import configparser
import os



config=configparser.RawConfigParser()
config.read(r"C:\Users\sivac\PycharmProjects\Python_SelRe\configurations\config.ini")

class Read_Config:
    @staticmethod
    def get_loginpage_url():
        url=config.get("test info","url")
        return url
    @staticmethod
    def get_username():
        username=config.get("test info","username")
        return username
    @staticmethod
    def get_password():
        password=config.get("test info","password")
        return password
