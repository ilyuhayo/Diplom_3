import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from data import UserData


class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("Ожидание формы входа")
    def wait_for_login_form(self):
        self.find_element_located_visibility(LoginPageLocators.LOGIN_FROM)

    @allure.step("Нажатие на ссылку восстановления пароля")
    def click_recovery_password_link(self):
        self.find_button_located_hard(LoginPageLocators.RECOVERY_PASSWORD_LINK).click()

    @allure.step("Ввод e-mail адреса")
    def input_email_field(self):
        self.find_element_located_visibility(LoginPageLocators.EMAIL_FIELD).send_keys(UserData.USER_EMAIL)

    @allure.step("Ввод пароля")
    def input_password_field(self):
        self.find_element_located_visibility(LoginPageLocators.PASSWORD_FIELD).send_keys(UserData.USER_PASSWORD)

    @allure.step("Нажатие на кнопку Вход")
    def click_enter_button(self):
        self.find_button_located_hard(LoginPageLocators.ENTER_BUTTON).click()
