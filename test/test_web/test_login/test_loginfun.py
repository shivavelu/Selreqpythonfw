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


'''if __name__=="__main__":
    print(Read_Config.get_loginpage_url())'''