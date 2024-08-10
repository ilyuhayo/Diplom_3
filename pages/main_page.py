from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def click_login_button(self):
        self.find_element_located(MainPageLocators.LOGIN_BUTTON_MAIN).click()
