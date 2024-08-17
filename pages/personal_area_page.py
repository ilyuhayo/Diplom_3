from pages.base_page import BasePage
from locators.personal_area_page_locators import PersonalAreaPageLocators
import allure


class PersonalAreaPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("Переход по ссылке История заказов")
    def click_order_history_section_button(self):
        self.find_button_located_hard(PersonalAreaPageLocators.ORDER_HISTORY_SECTION_BUTTON).click()

    @allure.step("Нажатие на кнопку Выход")
    def click_exit_from_account_button(self):
        self.find_button_located_hard(PersonalAreaPageLocators.EXIT_FROM_ACCOUNT_BUTTON).click()
