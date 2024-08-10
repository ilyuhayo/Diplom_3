from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __int__(self, driver):
        self.driver = driver

    def go_to_site(self, base_url):
        return self.driver.get(base_url)

    def find_element_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator),
                                                      message=f'Not found {locator}')

    def get_current_url(self):
        return self.driver.current_url
