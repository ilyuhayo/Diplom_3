from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators


class OrderFeedPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def check_order_feed_header_text(self):
        header_text = self.find_element_located(OrderFeedPageLocators.ORDER_FEED_HEADER_TEXT).text
        return header_text
