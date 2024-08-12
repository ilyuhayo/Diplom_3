from selenium.webdriver.common.by import By


class BasePageLocators:
    PERSONAL_AREA_BUTTON = (By.XPATH,
                            "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Личный Кабинет']")

    OVERLAY = (By.CSS_SELECTOR, "Modal_modal_overlay__x2ZCr")
