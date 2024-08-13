from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.base_page_locators import BasePageLocators


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def click_login_button(self):
        self.find_button_located_hard(MainPageLocators.LOGIN_BUTTON_MAIN).click()

    def click_personal_area_button(self):
        self.find_button_located_hard(BasePageLocators.PERSONAL_AREA_BUTTON).click()

    def click_order_feed_button(self):
        self.find_button_located_hard(BasePageLocators.ORDER_FEED_BUTTON).click()

    def click_constructor_button(self):
        self.find_button_located(BasePageLocators.CONSTRUCTOR_BUTTON).click()

    def click_r2_d3_bun_button(self):
        self.find_button_located_hard(MainPageLocators.R2_D3_BUN).click()

    def check_ingredient_detail_header_text(self):
        header_text = self.find_element_located(MainPageLocators.R2_D3_BUN_INGREDIENT_DETAILS_WINDOW_HEADER).text
        return header_text

    def click_close_window_detail_ingredient_button(self):
        self.find_button_located_hard(MainPageLocators.CLOSE_WINDOW_DETAILS_INGREDIENT_BUTTON).click()

    def check_make_burger_header_text(self):
        header_text = self.find_element_located(MainPageLocators.MAKE_BURGER_HEADER).text
        return header_text

    def drag_r2_d3_bun_to_constructor(self):
        self.drag_and_drop(MainPageLocators.R2_D3_BUN, MainPageLocators.DRAG_ORDER_CONSTRUCTOR)

    def check_ingredient_counter(self):
        header_text = self.find_element_located(MainPageLocators.INGREDIENT_COUNTER).text
        return header_text

    def click_make_order_button(self):
        self.find_button_located_hard(MainPageLocators.MAKE_ORDER_BUTTON).click()

    def check_order_status_text(self):
        order_status_text = self.find_button_located_hard(MainPageLocators.IDENTIFIER_ORDER_TEXT).text
        return order_status_text

    def check_order_number_on_order_created_window(self):
        order_status_text = self.find_button_located_hard(MainPageLocators.ORDER_NUMBER_ON_ORDER_CREATED_WINDOW).text
        return int(order_status_text)
