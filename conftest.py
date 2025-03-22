import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Specity the browser you want to run the test"
    )

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    global driver
    if browser=="chrome":
        driver=webdriver.Chrome()
    elif browser=="firefox":
        driver=webdriver.Firefox()
    elif browser=="ie":
        driver=webdriver.Ie()
    else:
        raise ValueError("Invalid browser")
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html=item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra= getattr(report,'extra',[])
    if report.when == 'call' or report.when == 'setup':
        xfail = hasattr(report,'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::","_")+".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)