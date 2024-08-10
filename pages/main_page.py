from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def click_login_button(self, locator):
        self.find_element_located(locator)
