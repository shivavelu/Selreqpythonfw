import pytest
from selenium.webdriver.chrome import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Specity the browser you want to run the test"
    )

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        driver=webdriver.Chrome()
    elif browser=="firefox":
        driver=webdriver.Firefox()
    elif browser=="ie":
        driver=webdriver.Ie()
    else:
        raise ValueError("Invalid browser")
    return driver