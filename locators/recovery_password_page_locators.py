from selenium.webdriver.common.by import By


class RecoveryPasswordPageLocators:
    EMAIL_FIELD = (By.XPATH, "//input[@class='text input__textfield text_type_main-default']")
    RESTORE_BUTTON = (By.XPATH,
                      "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    RESTORE_PASSWORD_HEADER_TEXT = (By.XPATH, "//h2[text()='Восстановление пароля']")
