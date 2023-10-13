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

@allure.epic("Карта")
@allure.feature('Проверка статистики')
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


@allure.epic("Карта")
@allure.feature('Тестирование фильтров ТТ/ТО')
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


@allure.epic("Карта")
@allure.feature('Тест-кейсы')
class TestCases:
    @allure.title('Тест-кейс: Поиск - переход в карточку НП')
    @allure.description('Переход в карточку Налогоплательщика через поиск на карте')
    def test_search_np(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        base_page = BasePage(browser)
        base_page.add_value(MapPageLocators.SEARCH_INPUT, SearchData.search_inn)
        time.sleep(1)
        base_page.click_on_element(MapPageLocators.SEARCH_BUTTON)
        time.sleep(3)
        base_page.wait_element_clickable(MapPageLocators.SEARCH_NP_BUTTON)
        base_page.click_on_element(MapPageLocators.SEARCH_NP_BUTTON)
        time.sleep(1)
        # Навести курсор на элемент SEARCH_NP_TEST_RESULT
        base_page.wait_element_clickable(MapPageLocators.SEARCH_NP_TEST_RESULT)
        search_np_test_result = base_page.find_element(MapPageLocators.SEARCH_NP_TEST_RESULT)
        ActionChains(browser).move_to_element(search_np_test_result).perform()
        time.sleep(1)
        base_page.wait_element_clickable(MapPageLocators.SEARCH_NP_TEST_CARD_BUTTON)
        base_page.click_on_element(MapPageLocators.SEARCH_NP_TEST_CARD_BUTTON)
        time.sleep(3)
        base_page.wait_element_visible(MapPageLocators.SEARCH_NP_TEST_CARD_HEADER)
        element = base_page.find_element(MapPageLocators.SEARCH_NP_TEST_CARD_HEADER)
        assert element.is_displayed(), "Переход в карточку НП не выполнен"

    @allure.title('Тест-кейс: Поиск - переход в карточку ККТ')
    @allure.description('Переход в карточку ККТ через поиск на карте')
    def test_search_kkt(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        base_page = BasePage(browser)
        base_page.add_value(MapPageLocators.SEARCH_INPUT, SearchData.search_inn)
        time.sleep(1)
        base_page.click_on_element(MapPageLocators.SEARCH_BUTTON)
        time.sleep(3)
        base_page.wait_element_clickable(MapPageLocators.SEARCH_NP_BUTTON)
        base_page.click_on_element(MapPageLocators.SEARCH_NP_BUTTON)
        time.sleep(1)
        # Навести курсор на элемент SEARCH_NP_TEST_RESULT
        base_page.wait_element_clickable(MapPageLocators.SEARCH_NP_TEST_RESULT)
        search_np_test_result = base_page.find_element(MapPageLocators.SEARCH_NP_TEST_RESULT)
        ActionChains(browser).move_to_element(search_np_test_result).perform()
        time.sleep(1)
        base_page.wait_element_clickable(MapPageLocators.SEARCH_NP_TEST_CARD_BUTTON)
        base_page.click_on_element(MapPageLocators.SEARCH_NP_TEST_CARD_BUTTON)
        time.sleep(3)
        base_page.wait_element_visible(MapPageLocators.SEARCH_NP_TEST_CARD_HEADER)
        element = base_page.find_element(MapPageLocators.SEARCH_NP_TEST_CARD_HEADER)
        assert element.is_displayed(), "Переход в карточку ККТ не выполнен"