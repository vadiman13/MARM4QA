from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data.urls import TestUrls
from data.creeds import VadlidCreeds, InvalidCreeds
from locators.locators import AuthorizationLocators, MapPageLocators
import time
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time
import allure


class AuthorizationPage(BasePage):

    @allure.step('Переход в форму авторизации')
    def go_to_autorization(self):
        self.open_authorization_url(TestUrls.AuthorizationPageUrl)


    # Переход на страницу авторизации
    @allure.step('Заполнение формы регистрации валидными данными')
    def valid_sign_marm(self):
        # Заполнение полей логина и пароля
        self.wait_element_visible(AuthorizationLocators.LOGIN_INPUT, 5)
        self.add_value(AuthorizationLocators.LOGIN_INPUT, VadlidCreeds.login)
        self.wait_element_visible(AuthorizationLocators.PASSWORD_INPUT, 5)
        self.add_value(AuthorizationLocators.PASSWORD_INPUT, VadlidCreeds.password)
        self.click_on_element(AuthorizationLocators.AUTH_BUTTON)
        self.wait_element_visible(MapPageLocators.MAP, 5)

    @allure.step('Заполнение формы регистрации невалидными данными')
    def invalid_sign_marm(self):
        # Заполнение полей логина и пароля
        self.wait_element_visible(AuthorizationLocators.LOGIN_INPUT, 5)
        self.add_value(AuthorizationLocators.LOGIN_INPUT, InvalidCreeds.login)
        self.wait_element_visible(AuthorizationLocators.PASSWORD_INPUT, 5)
        self.add_value(AuthorizationLocators.PASSWORD_INPUT, InvalidCreeds.password)
        self.click_on_element(AuthorizationLocators.AUTH_BUTTON)

    @allure.step('Ожидание ошибки')
    def wait_error_visible(self):
        self.wait_element_visible(AuthorizationLocators.ERROR, 5)

    @allure.step('Авторизация')
    def get_authorization(self):
        # Заполнение полей логина и пароля
        self.go_to_page(TestUrls.AuthorizationPageUrl)
        self.wait_element_visible(AuthorizationLocators.LOGIN_INPUT, 5)
        self.add_value(AuthorizationLocators.LOGIN_INPUT, VadlidCreeds.login)
        self.wait_element_visible(AuthorizationLocators.PASSWORD_INPUT, 5)
        self.add_value(AuthorizationLocators.PASSWORD_INPUT, VadlidCreeds.password)
        self.click_on_element(AuthorizationLocators.AUTH_BUTTON)
        self.wait_element_visible(MapPageLocators.MAP, 5)






