from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators.locators
from data.urls import TestUrls
from data.creeds import VadlidCreeds, InvalidCreeds
from data.data import SearchData
from locators.locators import AuthorizationLocators, MapPageLocators, EconomicsPageLocators, ReportsPageLocators, MarketonPageLocators, ClaimsPageLocators
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
from selenium.webdriver.common.action_chains import ActionChains



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







