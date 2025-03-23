import os
from datetime import datetime

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Specify the browser you want to run the test"
    )


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope='function')
def setup(browser):
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "ie":
        driver = webdriver.Ie()
    else:
        raise ValueError("Invalid browser")
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == 'setup':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            project_dir = os.path.dirname(os.path.abspath(__file__))
            screenshot_dir = os.path.join(project_dir, "screenshot")
            os.makedirs(screenshot_dir,exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"{item.name}_{timestamp}.png"
            screenshot_path = os.path.join(screenshot_dir, file_name)
            screenshot=_capture_screenshot(screenshot_path)
            extra.append(pytest_html.extras.image(screenshot, ''))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
    return driver.get_screenshot_as_base64() #the hero



if __name__=="__main__":
    project_dir = os.path.dirname(os.path.abspath(__file__))
    screenshot_dir = os.path.join(project_dir, "screenshot")
    print(screenshot_dir)
    screenshot_path = os.path.join(screenshot_dir,"test_login.png")
    print(screenshot_path)