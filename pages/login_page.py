from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def click_recovery_password_link(self):
        self.find_element_located(LoginPageLocators.RECOVERY_PASSWORD_LINK).click()
