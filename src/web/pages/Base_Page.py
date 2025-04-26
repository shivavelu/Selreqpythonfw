import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base_Page(object):
    def __init__(self, driver):
        self.local_directories = None
        self.driver = driver
        self.timeout = 30
        self.implicit_wait = 15

    def wait_till_specific_element_is_not_displayed(self, element):
        try:
            wait = WebDriverWait(self.driver, self.implicit_wait)
            expected_element = EC.visibility_of_element_located(element)
            wait.until(expected_element)
            return True
        except TimeoutError:
            raise

    def click_on_element(self, element):
        self.driver.find_element(*self.local_directories[element]).click()

    def get_text_from_element(self, element):
        try:
            time.sleep(10)
            wait = WebDriverWait(self.driver, 10)
            self.etext = wait.until(EC.presence_of_element_located(element))
            return self.etext.text
        except Exception as e:
            print(f"Error retrieving text: {e}")
            return None
        '''try:

            self.etext = self.driver.find_element(*self.local_directories[element])
           # self.etext = self.driver.find_element(*element)
        except KeyError:
            print("Element {} does not exist".format(element))
        text = self.etext.text
        return text'''

    def get_attr_value(self, element):
        try:
            a = self.driver.find_element(*self.local_directories[element])
            time.sleep(1)
        except KeyError:
            print("Element {} does not exist".format(element))
        text = a.get_attribute('value')
        return text

    def get_attr_title(self, element):
        try:
            a = self.driver.find_element(*self.local_directories[element])
            time.sleep(1)
        except KeyError:
            print("Element {} does not exist".format(element))
        text = a.get_attribute('title')
        return text

    def is_element_exists(self, element):
        try:
            self.driver.find_element(*self.local_directories[element])
            time.sleep(1)
            return 1
        except KeyError:
            print("Element {} does not exist".format(element))
        return 0

