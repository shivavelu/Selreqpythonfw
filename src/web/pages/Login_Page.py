import time
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.web.pages.Base_Page import Base_Page


class Login_Page(Base_Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.local_directories={"input_text_email":(By.ID,"email"),
                       "input_text_password":(By.ID,"password"),
                       "button_login":(By.ID,"submit"),
                       "button_logout":(By.ID,"logout"),
                       "text_Error":(By.ID,"error")
                      }

    def enter_username(self,username):
        self.driver.find_element(*self.local_directories["input_text_email"]).clear()
        self.driver.find_element(*self.local_directories["input_text_email"]).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(*self.local_directories["input_text_password"]).clear()
        self.driver.find_element(*self.local_directories["input_text_password"]).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.local_directories["button_login"]).click()

    def click_logout(self):
        self.driver.find_element(*self.local_directories["button_logout"]).click()

    def   getLoginError(self):
        # ele=self.driver.find_element(*self.local_directories["text_Error"])
        # time.sleep(10)
        # return ele.text
        return self.get_text_from_element(self.local_directories["text_Error"])





