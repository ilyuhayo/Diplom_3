import pytest
from conftest import browser
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.login_page import LoginPage
from locators.base_page_locators import BasePageLocators


class TestOrderFeedPage:
    def test_get_order_details_by_click_on_order(self, browser):
        main_page = MainPage(browser)
        main_page.go_to_site(BasePageLocators.MAIN_PAGE_URL)
        main_page.click_order_feed_button()
        order_feed_page = OrderFeedPage(browser)
        order_feed_page.click_on_first_order()
        assert order_feed_page.check_compound_order_text_on_detail_order_window() == "Cостав"

    def test_user_order_is_displayed_in_general_order_list(self, browser):
        main_page = MainPage(browser)
        main_page.go_to_site(BasePageLocators.MAIN_PAGE_URL)
        main_page.click_order_feed_button()
        order_feed_page = OrderFeedPage(browser)
        assert order_feed_page.check_my_order_in_general_order_list() == "#0105517"

    def test_check_order_counter_by_all_time_is_increase_by_making_order(self, browser):
        main_page = MainPage(browser)
        main_page.go_to_site(BasePageLocators.MAIN_PAGE_URL)
        main_page.click_order_feed_button()
        order_feed_page = OrderFeedPage(browser)
        initial_counter_value = order_feed_page.check_orders_done_by_all_time_counter_origin_value()
        main_page.click_constructor_button()
        main_page.click_login_button()
        login_page = LoginPage(browser)
        login_page.input_email_field()
        login_page.input_password_field()
        login_page.click_enter_button()
        main_page.drag_r2_d3_bun_to_constructor()
        main_page.click_make_order_button()
        main_page.click_close_window_detail_ingredient_button()
        main_page.click_order_feed_button()
        final_counter_value = order_feed_page.check_orders_done_by_all_time_counter_after_make_order_value()
        assert final_counter_value == initial_counter_value + 1

    def test_check_order_counter_by_today_is_increase_by_making_order(self, browser):
        main_page = MainPage(browser)
        main_page.go_to_site(BasePageLocators.MAIN_PAGE_URL)
        main_page.click_order_feed_button()
        order_feed_page = OrderFeedPage(browser)
        initial_counter_value = order_feed_page.check_orders_done_by_today_counter_origin_value()
        main_page.click_constructor_button()
        main_page.click_login_button()
        login_page = LoginPage(browser)
        login_page.input_email_field()
        login_page.input_password_field()
        login_page.click_enter_button()
        main_page.drag_r2_d3_bun_to_constructor()
        main_page.click_make_order_button()
        main_page.click_close_window_detail_ingredient_button()
        main_page.click_order_feed_button()
        final_counter_value = order_feed_page.check_orders_done_today_counter_after_make_order_value()
        assert final_counter_value == initial_counter_value + 1

    def test_check_order_number_in_the_work_panel_after_making_order(self, browser):
        main_page = MainPage(browser)
        main_page.go_to_site(BasePageLocators.MAIN_PAGE_URL)
        main_page.click_login_button()
        login_page = LoginPage(browser)
        login_page.input_email_field()
        login_page.input_password_field()
        login_page.click_enter_button()
        main_page.drag_r2_d3_bun_to_constructor()
        main_page.click_make_order_button()
        main_page.check_order_status_text()
        order_number_on_main = main_page.check_order_number_on_order_created_window()
        main_page.click_close_window_detail_ingredient_button()
        main_page.click_order_feed_button()
        order_feed_page = OrderFeedPage(browser)
        order_number_on_feed = order_feed_page.check_order_number_in_the_work_panel()
        assert order_number_on_main == order_number_on_feed
