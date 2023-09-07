from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators.locators
from data.urls import TestUrls
from data.creeds import VadlidCreeds, InvalidCreeds
from locators.locators import AuthorizationLocators, MapPageLocators, EconomicsPageLocators, ReportsPageLocators
import time
from pages.base_page import BasePage
from pages.authorization_page import AuthorizationPage
from pages.map_page import MapPage
from data.data import StatisticExpected
from selenium.webdriver.common.by import By
import time
import allure

class TestStatisticInfo:
    @allure.title('Проверка статистических показателей НП')
    @allure.description('Проверка кол-ва НП')
    def test_statistic_np(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        map_page = MapPage(browser)
        text = map_page.get_np()
        expected_np = StatisticExpected.statistic_np
        assert int(text) > expected_np, f"Число налогоплательщиков - '{text}' менее минимального значения - {expected_np}"

    @allure.title('Проверка статистических показателей ККТ')
    @allure.description('Проверка кол-ва ККТ')
    def test_statistic_kkt(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        map_page = MapPage(browser)
        text = map_page.get_kkt()
        expected_np = StatisticExpected.statistic_np
        assert int(text) > expected_np, f"Число ККТ - '{text}' менее минимального значения - {expected_np}"

class TestMapPage:
    @allure.title('Проверка фильтра ТО/ТТ')
    @allure.description('Проверка открытия формы фильтров при клике на кнопку "Фильтры"')
    def test_filters_panel(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        map_page = MapPage(browser)
        map_page.filter_button_click()
        element = map_page.find_map_element(MapPageLocators.FILTERS_FORM)
        assert element.is_displayed(), "Форма фильтров не отображается"

