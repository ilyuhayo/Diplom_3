from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators


class OrderFeedPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def check_order_feed_header_text(self):
        header_text = self.find_element_located(OrderFeedPageLocators.ORDER_FEED_HEADER_TEXT).text
        return header_text

    def click_on_first_order(self):
        self.find_element_located(OrderFeedPageLocators.FIRST_ORDER_IN_ORDER_LIST).click()

    def check_my_order_in_general_order_list(self):
        order_element = self.find_element_located(OrderFeedPageLocators.ORDER_NUMBER_0105453)

        self.browser.execute_script("arguments[0].scrollIntoView();", order_element)

        return order_element.text

    def check_compound_order_text_on_detail_order_window(self):
        header_text = self.find_element_located(OrderFeedPageLocators.COMPOUND_ORDER_TEXT).text
        return header_text

    def check_orders_done_by_all_time_counter_origin_value(self):
        header_text = self.find_element_located(OrderFeedPageLocators.ORDERS_DONE_BY_ALL_TIME_COUNTER).text
        return int(header_text)

    def check_orders_done_by_all_time_counter_after_make_order_value(self):
        header_text = self.find_element_located(OrderFeedPageLocators.ORDERS_DONE_BY_ALL_TIME_COUNTER).text
        return int(header_text)

    def check_orders_done_by_today_counter_origin_value(self):
        header_text = self.find_element_located(OrderFeedPageLocators.ORDERS_DONE_BY_TODAY_COUNTER).text
        return int(header_text)

    def check_orders_done_today_counter_after_make_order_value(self):
        header_text = self.find_element_located(OrderFeedPageLocators.ORDERS_DONE_BY_TODAY_COUNTER).text
        return int(header_text)

    def check_order_number_in_the_work_panel(self):
        header_text = self.find_button_located_hard(OrderFeedPageLocators.ORDER_NUMBER_IN_THE_WORK_PANEL).text
        return int(header_text)
