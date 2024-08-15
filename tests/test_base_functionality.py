import pytest
from conftest import browser
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.login_page import LoginPage
from locators.base_page_locators import BasePageLocators
from urls import URLS


class TestBaseFunctionality:
    def test_go_to_order_feed(self, browser):
        main_page = MainPage(browser)
        main_page.go_to_site(URLS.MAIN_PAGE_URL)
        main_page.click_order_feed_button()
        order_feed_page = OrderFeedPage(browser)
        assert order_feed_page.check_order_feed_header_text() == "Лента заказов"


    def test_go_to_constructor(self, browser):
        main_page = MainPage(browser)
        main_page.go_to_site(URLS.MAIN_PAGE_URL)
        main_page.click_order_feed_button()
        main_page.click_constructor_button()
        assert main_page.get_current_url() == URLS.MAIN_PAGE_URL

    def test_get_ingredient_details_window_by_click_on_ingredient(self, browser):
        main_page = MainPage(browser)
        main_page.go_to_site(URLS.MAIN_PAGE_URL)
        main_page.click_r2_d3_bun_button()
        assert main_page.check_ingredient_detail_header_text() == "Детали ингредиента"

    def test_close_ingredient_detail_window(self, browser):
        main_page = MainPage(browser)
        main_page.go_to_site(URLS.MAIN_PAGE_URL)
        main_page.click_r2_d3_bun_button()
        main_page.click_close_window_detail_ingredient_button()
        assert main_page.check_make_burger_header_text() == "Соберите бургер"

    def test_increase_ingredient_counter_by_add_ingredient_to_order(self, browser):
        main_page = MainPage(browser)
        main_page.go_to_site(URLS.MAIN_PAGE_URL)
        main_page.drag_r2_d3_bun_to_constructor()
        assert main_page.check_ingredient_counter() == "2"

    def test_login_user_can_create_order(self, browser):
        main_page = MainPage(browser)
        main_page.go_to_site(URLS.MAIN_PAGE_URL)
        main_page.click_login_button()
        login_page = LoginPage(browser)
        login_page.input_email_field()
        login_page.input_password_field()
        login_page.click_enter_button()
        main_page.click_make_order_button()
        main_page.check_order_status_text()
        assert main_page.check_order_status_text() == "идентификатор заказа"



