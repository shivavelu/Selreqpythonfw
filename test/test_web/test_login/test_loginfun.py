import time

from fwutilities.json_utility import JSON_Utility
from fwutilities.log_utility import Log_Maker
from fwutilities.readconfig_utiltiy import Read_Config
from src.web.pages.Login_Page import Login_Page
from conftest import *


class TestLogin:
    applciation_url=Read_Config.get_loginpage_url()
    LOGGER=Log_Maker.log_gen()


    def test_login(self,setup):
        self.LOGGER.info("TestLogin.test_login")
        driver=setup
        driver.get(self.applciation_url)
        login_page=Login_Page(driver)
        self.LOGGER.info("Navigated to the application")
        driver.implicitly_wait(10)
        driver.maximize_window()
        login_page.enter_username(Read_Config.get_username())
        login_page.enter_password(Read_Config().get_password())
        login_page.click_login()
        login_page.click_logout()
        self.LOGGER.info("Closed the browser")

    @pytest.mark.parametrize("test_case", JSON_Utility.load_test_data())
    def test_login_withtestdata(self, setup, test_case):
        self.LOGGER.info("TestLogin.test_login_withtestdata")
        driver=setup
        driver.get(self.applciation_url)
        login_page=Login_Page(driver)
        self.LOGGER.info("Navigated to the application")
        driver.implicitly_wait(10)
        driver.maximize_window()
        login_page.enter_username(test_case["username"])
        login_page.enter_password(test_case["password"])
        login_page.click_login()  # Add a 2-second delay
        time.sleep(10)
        actual_error=login_page.getLoginError()
        expected_error=test_case["expected_error"]
        assert actual_error == expected_error, f"Expected '{expected_error}', but got '{actual_error}'"



'''if __name__=="__main__":
    print(Read_Config.get_loginpage_url())'''