class TestLogin:
    def test_login1(self,setup):
        driver=setup
        driver.get("https://redbus.com")
        assert 1==2

