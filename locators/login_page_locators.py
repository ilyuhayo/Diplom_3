from selenium.webdriver.common.by import By


class LoginPageLocators:
    RECOVERY_PASSWORD_LINK = (By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Восстановить пароль']")
