from data.urls import TestUrls
from pages.authorization_page import AuthorizationPage
from pages.base_page import BasePage
from locators.locators import AuthorizationLocators, MapPageLocators, BasePageLocators
import allure
import time




@allure.epic("Авторизация")
@allure.feature("Проверка авторизации")
class TestAuthorizationForm:

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


@allure.epic("Авторизация")
@allure.feature("Проверка перехода в форму авторизации")
class TestBackAuthorizationPage:

    @allure.title("Возврат в форму авторизации")
    @allure.description('Проверка возврата в форму авторизации при клике на логотип АСК ККТ')
    def test_back_to_authorization(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.go_to_autorization()
        authorization_page.valid_sign_marm()
        base_page = BasePage(browser)
        base_page.wait_element_visible(MapPageLocators.ASK_KKT_LOGO)
        base_page.click_on_element(MapPageLocators.ASK_KKT_LOGO)
        base_page.find_element_visible(AuthorizationLocators.AUTHORIZATION_FORM)
        element = base_page.find_element(AuthorizationLocators.AUTHORIZATION_FORM)
        assert element.is_displayed(), "Не осуществлен возврат в форму авторизации"

    @allure.title("Выход из учетной записи")
    @allure.description('Проверка выхода из учетной записи после клика на кнопку "Выйти"')
    def test_logout(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.go_to_autorization()
        authorization_page.valid_sign_marm()
        base_page = BasePage(browser)
        base_page.wait_element_visible(BasePageLocators.LOGOUT_BUTTON)
        base_page.click_on_element(BasePageLocators.LOGOUT_BUTTON)
        base_page.find_element_visible(AuthorizationLocators.AUTHORIZATION_FORM)
        element = base_page.find_element(AuthorizationLocators.AUTHORIZATION_FORM)
        assert element.is_displayed(), "Не осуществлен выход из учетной записи"



