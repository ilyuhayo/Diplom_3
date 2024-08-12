from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def wait_for_login_form(self):
        self.find_element_located(LoginPageLocators.LOGIN_FROM)

    def click_recovery_password_link(self):
        self.find_button_located(LoginPageLocators.RECOVERY_PASSWORD_LINK).click()

    def input_email_field(self):
        self.find_element_located(LoginPageLocators.EMAIL_FIELD).send_keys("zolotov_10@mail.ru")

    def input_password_field(self):
        self.find_element_located(LoginPageLocators.PASSWORD_FIELD).send_keys("123456")

    def click_enter_button(self):
        self.find_button_located(LoginPageLocators.ENTER_BUTTON).click()
