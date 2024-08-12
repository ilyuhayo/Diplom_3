import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    browser_name = request.param
    browser = None

    if browser_name == "chrome":
        options = ChromeOptions()
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()
        browser = webdriver.Firefox(options=options)

    else:
        raise pytest.UsageError("Unsupported browser: {}".format(browser_name))

    yield browser
    browser.quit()
