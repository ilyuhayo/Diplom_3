from selenium.webdriver.common.by import By


class PersonalAreaPageLocators:
    ORDER_HISTORY_PAGE_URL = "https://stellarburgers.nomoreparties.site/account/order-history"
    ORDER_HISTORY_SECTION_BUTTON = (
        By.XPATH,
        "//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive' and text()='История заказов']")

    EXIT_FROM_ACCOUNT_BUTTON = (
        By.XPATH, "//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']")
