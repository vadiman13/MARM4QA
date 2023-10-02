from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators.locators
from data.urls import TestUrls
from data.creeds import VadlidCreeds, InvalidCreeds
from locators.locators import AuthorizationLocators, MapPageLocators, EconomicsPageLocators, ReportsPageLocators, MarketonPageLocators, ClaimsPageLocators, AutonomusPageLocators
import time
from pages.base_page import BasePage
from pages.authorization_page import AuthorizationPage
from pages.claims_page import ClaimsPage
from pages.marketon_page import MarketonPage
from pages.map_page import MapPage
from data.data import StatisticExpected
from selenium.webdriver.common.by import By
import time
import allure

class TestAutonomusPage:
    @allure.title('Проверка кнопки добавления АТ')
    @allure.description('Проверка отображения кнопки добавления АТ в шапке раздела')
    def test_add_button(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        base_page = BasePage(browser)
        base_page.go_to_page(TestUrls.ControlAutonomousRegisterPageUrl)
        element = base_page.find_element_visible(AutonomusPageLocators.CONTROL_AUTONOMOUS_BUTTON_ADD_AT)
        assert element.is_displayed(), 'Кнопка добавления АТ не отображена'

    @allure.title('Проверка кнопки выгрузки логов')
    @allure.description('Проверка отображения кнопки выгрузки логов')
    def test_download_button(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        base_page = BasePage(browser)
        base_page.go_to_page(TestUrls.ControlAutonomousRegisterPageUrl)
        element = base_page.find_element_visible(AutonomusPageLocators.CONTROL_AUTONOMOUS_BUTTON_UNLOADING_LOGS)
        assert element.is_displayed(), 'Кнопка выгрузки логов не отображена'

    @allure.title('Проверка кнопки сброса фильтров')
    @allure.description('Проверка отображения сброса фильтров')
    def test_reset_button(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        base_page = BasePage(browser)
        base_page.go_to_page(TestUrls.ControlAutonomousRegisterPageUrl)
        element = base_page.find_element_visible(AutonomusPageLocators.CONTROL_AUTONOMOUS_BUTTON_RESET_FILTER)
        assert element.is_displayed(), 'Кнопка выгрузки логов не отображена'

    @allure.title('Проверка панели фильтров АТ')
    @allure.description('Проверка отображения панели фильтров АТ')
    def test_filter_panel(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        base_page = BasePage(browser)
        base_page.go_to_page(TestUrls.ControlAutonomousRegisterPageUrl)
        element = base_page.find_element_visible(AutonomusPageLocators.CONTROL_AUTONOMOUS_FILTERS_PANEL)
        assert element.is_displayed(), 'Панель фильтров не отображена'

    @allure.title('Проверка таблицы АТ')
    @allure.description('Проверка отображения таблицы АТ')
    def test_autonomus_table(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        base_page = BasePage(browser)
        base_page.go_to_page(TestUrls.ControlAutonomousRegisterPageUrl)
        element = base_page.find_element_visible(AutonomusPageLocators.CONTROL_AUTONOMOUS_TABLE_AT)
        assert element.is_displayed(), 'Таблица АТ не отображена'

    # @allure.title('Проверка перехода в карточку АТ')
    # @allure.description('Переход в карточку АТ через таблицу')
    # def test_autonomus_cart_open(self, browser):
    #     authorization_page = AuthorizationPage(browser)
    #     authorization_page.get_authorization()
    #     base_page = BasePage(browser)
    #     base_page.go_to_page(TestUrls.ControlAutonomousRegisterPageUrl)
    #     base_page.click_on_element(AutonomusPageLocators.CONTROL_AUTONOMOUS_CARD_TEST)
    #     element = base_page.find_element_visible(AutonomusPageLocators.CONTROL_AUTONOMOUS_CARD_TREE)
    #     assert element.is_displayed(), 'Переход в карточку АТ не осуществлен'