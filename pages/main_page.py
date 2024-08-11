from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def click_login_button(self):
        self.find_button_located(MainPageLocators.LOGIN_BUTTON_MAIN).click()
