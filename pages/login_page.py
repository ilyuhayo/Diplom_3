from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def click_recovery_password_link(self):
        self.find_button_located(LoginPageLocators.RECOVERY_PASSWORD_LINK).click()
