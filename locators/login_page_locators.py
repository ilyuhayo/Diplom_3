from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_PAGE_URL = "https://stellarburgers.nomoreparties.site/login"
    RECOVERY_PASSWORD_LINK = (By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Восстановить пароль']")
    EMAIL_FIELD = (By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @name='name']")
    PASSWORD_FIELD = (By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @name='Пароль']")
    ENTER_BUTTON = (
        By.XPATH,
        "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    LOGIN_FROM = (By.XPATH, "//div[@class='Auth_login__3hAey']")
