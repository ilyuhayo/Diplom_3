from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators
import allure


class OrderFeedPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("Проверка заголовка Лента заказов на странице Лента заказов")
    def check_order_feed_header_text(self):
        header_text = self.find_element_located_visibility(OrderFeedPageLocators.ORDER_FEED_HEADER_TEXT).text
        return header_text

    @allure.step("Нажатие на первый заказ в списке заказов")
    def click_on_first_order(self):
        self.find_button_located_hard(OrderFeedPageLocators.FIRST_ORDER_IN_ORDER_LIST).click()

    @allure.step("Проверка созданного заказа в списке заказов")
    def check_my_order_in_general_order_list(self):
        order_element = self.find_element_located_hard(OrderFeedPageLocators.ORDER_NUMBER_0107084)
        return order_element.text

    @allure.step("Проверка наличия поля Состав на карточке информации по заказу")
    def check_compound_order_text_on_detail_order_window(self):
        header_text = self.find_element_located_visibility(OrderFeedPageLocators.COMPOUND_ORDER_TEXT).text
        return header_text

    @allure.step("Проверка счетчика Выполнено за все время")
    def check_orders_done_by_all_time_counter_origin_value(self):
        header_text = self.find_element_located_visibility(OrderFeedPageLocators.ORDERS_DONE_BY_ALL_TIME_COUNTER).text
        return int(header_text)

    @allure.step("Проверка счетчика Выполнено за все время после создания заказа")
    def check_orders_done_by_all_time_counter_after_make_order_value(self):
        header_text = self.find_element_located_visibility(OrderFeedPageLocators.ORDERS_DONE_BY_ALL_TIME_COUNTER).text
        return int(header_text)

    @allure.step("Проверка счетчика Выполнено за сегодня")
    def check_orders_done_by_today_counter_origin_value(self):
        header_text = self.find_element_located_visibility(OrderFeedPageLocators.ORDERS_DONE_BY_TODAY_COUNTER).text
        return int(header_text)

    @allure.step("Проверка счетчика Выполнено за сегодня после создания заказа")
    def check_orders_done_today_counter_after_make_order_value(self):
        header_text = self.find_element_located_visibility(OrderFeedPageLocators.ORDERS_DONE_BY_TODAY_COUNTER).text
        return int(header_text)

    @allure.step("Проверка номера заказа на панели В работе")
    def check_order_number_in_the_work_panel(self):
        header_text = self.find_element_located_visibility(OrderFeedPageLocators.ORDER_NUMBER_IN_THE_WORK_PANEL).text
        return int(header_text)
