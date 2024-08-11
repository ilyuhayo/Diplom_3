from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def go_to_site(self, base_url):
        return self.browser.get(base_url)

    def find_element_located(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator))

    def find_button_located(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.element_to_be_clickable(locator))

    def get_current_url(self):
        return self.browser.current_url
