from pages.base_page import BasePage
from locators.recovery_password_page_locators import RecoveryPasswordPageLocators
from data import UserData


class RecoveryPasswordPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def input_email_field(self):
        self.find_element_located_visibility(RecoveryPasswordPageLocators.EMAIL_FIELD).send_keys(UserData.USER_EMAIL)

    def click_restore_button(self):
        self.find_button_located(RecoveryPasswordPageLocators.RESTORE_BUTTON).click()

    def check_restore_password_header_text(self):
        header_text = self.find_element_located_visibility(RecoveryPasswordPageLocators.RESTORE_PASSWORD_HEADER_TEXT).text
        return header_text

    def input_password_field(self):
        self.find_element_located_visibility(RecoveryPasswordPageLocators.PASSWORD_FIELD).send_keys(UserData.USER_PASSWORD)

    def click_view_password_button(self):
        self.find_button_located_hard(RecoveryPasswordPageLocators.VIEW_PASSWORD_BUTTON).click()

    def get_active_password_field(self):
        active_password_field = self.find_element_located_visibility(RecoveryPasswordPageLocators.PASSWORD_FIELD_ACTIVE)
        return active_password_field


