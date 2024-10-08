import pytest
from conftest import browser
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.recovery_password_page import RecoveryPasswordPage
import allure
from urls import URLS


class TestRecoveryPasswordPage:
    @allure.title("Переход на страницу восстановление пароля по кнопке Восстановить пароль")
    def test_go_to_recovery_password_page_by_recovery_password_link(self, browser):
        main_page = MainPage(browser)
        main_page.go_to_site(URLS.MAIN_PAGE_URL)
        main_page.click_login_button()
        login_page = LoginPage(browser)
        login_page.click_recovery_password_link()
        assert login_page.get_current_url() == URLS.FORGOT_PASSWORD_PAGE_URL


    @allure.title("Ввод почты на странице восстановления пароля и нажатие на кнопку Восстановить")
    def test_input_email_and_click_reset_button(self, browser):
        main_page = MainPage(browser)
        main_page.go_to_site(URLS.MAIN_PAGE_URL)
        main_page.click_login_button()
        login_page = LoginPage(browser)
        login_page.click_recovery_password_link()
        recovery_password_page = RecoveryPasswordPage(browser)
        recovery_password_page.input_email_field()
        recovery_password_page.click_restore_button()
        assert recovery_password_page.check_restore_password_header_text() == "Восстановление пароля"


    @allure.title("Нажатие на кнопку показать/скрыть пароль подсвечивает поле пароль")
    def test_check_password_in_field_by_view_password_button(self, browser):
        main_page = MainPage(browser)
        main_page.go_to_site(URLS.MAIN_PAGE_URL)
        main_page.click_login_button()
        login_page = LoginPage(browser)
        login_page.click_recovery_password_link()
        recovery_password_page = RecoveryPasswordPage(browser)
        recovery_password_page.input_email_field()
        recovery_password_page.click_restore_button()
        recovery_password_page.input_password_field()
        recovery_password_page.click_view_password_button()
        assert recovery_password_page.get_active_password_field()

