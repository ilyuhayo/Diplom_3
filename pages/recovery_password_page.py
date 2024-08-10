from pages.base_page import BasePage
from locators.recovery_password_page_locators import RecoveryPasswordPageLocators


class RecoveryPasswordPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def input_email_field(self):
        self.find_element_located(RecoveryPasswordPageLocators.EMAIL_FIELD).send_keys("zolotov_10@mail.ru")

    def click_restore_button(self):
        self.find_button_located(RecoveryPasswordPageLocators.RESTORE_BUTTON).click()

    def check_restore_password_header_text(self):
        header_text = self.find_element_located(RecoveryPasswordPageLocators.RESTORE_PASSWORD_HEADER_TEXT).text
        return header_text
