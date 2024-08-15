from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.base_page_locators import BasePageLocators
import allure


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("Нажатие на кнопку Войти в аккаунт")
    def click_login_button(self):
        self.find_button_located_hard(MainPageLocators.LOGIN_BUTTON_MAIN).click()

    @allure.step("Нажатие на кнопку Личный кабинет")
    def click_personal_area_button(self):
        self.find_button_located_hard(BasePageLocators.PERSONAL_AREA_BUTTON).click()

    @allure.step("Нажатие на кнопку Лента заказов")
    def click_order_feed_button(self):
        self.find_button_located_hard(BasePageLocators.ORDER_FEED_BUTTON).click()

    @allure.step("Нажатие на кнопку Конструктор")
    def click_constructor_button(self):
        self.find_button_located(BasePageLocators.CONSTRUCTOR_BUTTON).click()

    @allure.step("Нажатие на Флюоресцентная булка R2-D3")
    def click_r2_d3_bun_button(self):
        self.find_button_located_hard(MainPageLocators.R2_D3_BUN).click()

    @allure.step("Проверка заголовка Детали ингредиента на карточке ингредиента")
    def check_ingredient_detail_header_text(self):
        header_text = self.find_element_located_visibility(MainPageLocators.R2_D3_BUN_INGREDIENT_DETAILS_WINDOW_HEADER).text
        return header_text

    @allure.step("Закрытие окна с ингредиентом")
    def click_close_window_detail_ingredient_button(self):
        self.find_button_located_hard(MainPageLocators.CLOSE_WINDOW_DETAILS_INGREDIENT_BUTTON).click()

    @allure.step("Проверка заголовка Соберите бургер на главной странице")
    def check_make_burger_header_text(self):
        header_text = self.find_element_located_visibility(MainPageLocators.MAKE_BURGER_HEADER).text
        return header_text

    @allure.step("Добавление ингредиента Флюоресцентная булка R2-D3 в заказ")
    def drag_r2_d3_bun_to_constructor(self):
        self.drag_and_drop(MainPageLocators.R2_D3_BUN, MainPageLocators.DRAG_ORDER_CONSTRUCTOR)

    @allure.step("Проверка счетчика на количество ингредиентов")
    def check_ingredient_counter(self):
        header_text = self.find_element_located_visibility(MainPageLocators.INGREDIENT_COUNTER).text
        return header_text

    @allure.step("Нажатие на кнопку Оформить заказ")
    def click_make_order_button(self):
        self.find_button_located_hard(MainPageLocators.MAKE_ORDER_BUTTON).click()

    @allure.step("Проверка поля идентификатор заказа в окне созданного заказа")
    def check_order_status_text(self):
        order_status_text = self.find_element_located_visibility(MainPageLocators.IDENTIFIER_ORDER_TEXT).text
        return order_status_text

    @allure.step("Проверка номера заказа в окне созданного заказа")
    def check_order_number_on_order_created_window(self):
        order_status_text = self.find_element_located_visibility(MainPageLocators.ORDER_NUMBER_ON_ORDER_CREATED_WINDOW).text
        return int(order_status_text)

    @allure.step("Ожидание пока номера заказа 9999 пропадет и появится актуальный номер заказа в окне созданного заказа")
    def wait_for_9999_number_disappear_on_created_order_window(self):
        self.wait_for_order_number_change(MainPageLocators.ORDER_NUMBER_ON_ORDER_CREATED_WINDOW)


