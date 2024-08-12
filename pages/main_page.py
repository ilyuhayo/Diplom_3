from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.base_page_locators import BasePageLocators


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def click_login_button(self):
        self.find_button_located_hard(MainPageLocators.LOGIN_BUTTON_MAIN).click()

    def click_personal_area_button(self):
        self.find_button_located_hard(BasePageLocators.PERSONAL_AREA_BUTTON).click()
