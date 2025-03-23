from selenium.webdriver.common.by import By


class Login_Page:
    local_directories={"input_text_email":[By.ID,"email"],
                       "input_text_password":[By.ID,"password"],
                       "button_login":[By.ID,"submit"],
                       "button_logout":[By.ID,"logout"],
                      }

    def __init__(self,driver):
        self.driver=driver

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
