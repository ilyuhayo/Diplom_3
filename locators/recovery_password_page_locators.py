from selenium.webdriver.common.by import By


class RecoveryPasswordPageLocators:
    FORGOT_PASSWORD_PAGE_URL = "https://stellarburgers.nomoreparties.site/forgot-password"
    EMAIL_FIELD = (By.XPATH, "//input[@class='text input__textfield text_type_main-default']")
    RESTORE_BUTTON = (By.XPATH,
                      "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    RESTORE_PASSWORD_HEADER_TEXT = (By.XPATH, "//h2[text()='Восстановление пароля']")
    PASSWORD_FIELD = (By.XPATH,
                      "//input[@class='text input__textfield text_type_main-default' and @name='Введите новый пароль']")
    VIEW_PASSWORD_BUTTON = (By.XPATH, "//div[@class='input__icon input__icon-action']")
    PASSWORD_FIELD_ACTIVE = (By.XPATH,
                             "//div[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']")