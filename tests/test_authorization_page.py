from data.urls import TestUrls
from pages.authorization_page import AuthorizationPage
from pages.base_page import BasePage
from locators.locators import AuthorizationLocators, MapPageLocators
import allure
import time



class TestAuthorizationPage:

    @allure.title("Успешная авторизация")
    @allure.description("Проверка авторизации с валидными данными, переход в МАРМ")
    def test_valid_authorization(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.go_to_autorization()
        authorization_page.valid_sign_marm()
        assert TestUrls.AuthorizationComplatedPageUrl in browser.current_url, "Авторизация не пройдена"

    @allure.title("Авторизация с невалидными данными")
    @allure.description("Проверка авторизации с невалидными данными, отображение ошибки")
    def test_invalid_authorization(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.go_to_autorization()
        authorization_page.invalid_sign_marm()
        authorization_page.wait_error_visible()
        assert authorization_page.find_element(AuthorizationLocators.ERROR), "Не отображена ошибка авторизации"

    @allure.title("Выход из учетной записи")
    @allure.description('Проверка выхода из учетной записи при клике на кнопку "Выйти"')
    def test_logout(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.go_to_autorization()
        authorization_page.valid_sign_marm()
        authorization_page.logout()
        assert TestUrls.AuthorizationPageUrl in browser.current_url, "Выход из учетной записи не осуществлен"




