from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators
from time import sleep


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def go_to_site(self, base_url):
        return self.browser.get(base_url)

    def find_element_located(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator))

    def find_button_located(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.element_to_be_clickable(locator))

    def find_button_located_hard(self, locator, time=10):
        WebDriverWait(self.browser, 20).until(EC.invisibility_of_element_located(BasePageLocators.OVERLAY))
        element = WebDriverWait(self.browser, time).until(EC.visibility_of_element_located(locator))
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
        element = WebDriverWait(self.browser, time).until(EC.element_to_be_clickable(locator))
        sleep(1)
        return element

    def get_current_url(self):
        return self.browser.current_url

