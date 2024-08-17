from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def go_to_site(self, base_url):
        self.browser.get(base_url)

    def find_element_located_presence(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator))

    def find_element_located_visibility(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.visibility_of_element_located(locator))

    def find_element_located_hard(self, locator, time=20):
        try:
            self.wait_for_overlay_to_disappear()
            element = WebDriverWait(self.browser, time).until(EC.visibility_of_element_located(locator))
            self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
            element = WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator))
            return element
        except TimeoutException:
            raise Exception("Элемент не найден или невидим!")

    def find_button_located(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.element_to_be_clickable(locator))

    def find_button_located_hard(self, locator, time=20):
        try:
            self.wait_for_overlay_to_disappear()
            element = self.wait_for_element_to_be_clickable(locator, time)
            return element
        except TimeoutException:
            raise Exception("Элемент не найден или не кликабелен!")

    def get_current_url(self):
        return self.browser.current_url

    def drag_and_drop(self, source_locator, target_locator, time=10):
        source_element = self.find_element_located_hard(source_locator, time)
        target_element = self.find_element_located_hard(target_locator, time)

        actions = ActionChains(self.browser)
        actions.drag_and_drop(source_element, target_element).perform()

    def wait_for_overlay_to_disappear(self, time=20):
        WebDriverWait(self.browser, time).until(EC.invisibility_of_element_located(BasePageLocators.OVERLAY))

    def wait_for_element_to_be_clickable(self, locator, time=20):
        element = WebDriverWait(self.browser, time).until(EC.visibility_of_element_located(locator))
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
        return WebDriverWait(self.browser, time).until(EC.element_to_be_clickable(locator))

    def wait_for_order_number_change(self, locator, time=20):
        def _order_number_changed(driver):
            element = self.find_element_located_visibility(locator)
            order_number = element.text
            return order_number != '9999'

        try:
            WebDriverWait(self.browser, time).until(_order_number_changed)
        except TimeoutException:
            raise Exception("Номер заказа не изменился!")
