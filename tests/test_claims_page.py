from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators.locators
from data.urls import TestUrls
from data.creeds import VadlidCreeds, InvalidCreeds
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

class TestClaimsSummary:

    @allure.title('Проверка диаграмм статистики жалоб')
    @allure.description('Проверка отображения диаграмм статистики жалоб')
    def test_claims_summary_diagram(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        claims_page = ClaimsPage(browser)
        claims_page.go_to_claims_summary()
        base_page = BasePage(browser)
        element = base_page.find_element_visible(ClaimsPageLocators.CONTROL_COMPLAINTS_SUMMARY_DIAGRAM_STATISTIC_COMPLAINTS)
        assert element.is_displayed(), 'Сводка кол-ва жалоб не отображена'

    @allure.title('Проверка диаграммы динамики жалоб')
    @allure.description('Проверка отображения диаграммы динамики жалоб')
    def test_claims_summary_dynamic_diagram(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        claims_page = ClaimsPage(browser)
        claims_page.go_to_claims_summary()
        base_page = BasePage(browser)
        element = base_page.find_element_visible(ClaimsPageLocators.CONTROL_COMPLAINTS_SUMMARY_DIAGRAM_DYNAMICS_COMPLAINTS)
        assert element.is_displayed(), 'График динамики жалоб не отображен'

    @allure.title('Проверка селектора периода динамики жалоб')
    @allure.description('Проверка селектора периода динамики жалоб')
    def test_claims_summary_dynamic_diagram_date_selector(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        claims_page = ClaimsPage(browser)
        claims_page.go_to_claims_summary()
        base_page = BasePage(browser)
        base_page.scroll_to(ClaimsPageLocators.CONTROL_COMPLAINTS_SUMMARY_SELECTOR_DATE)
        element = base_page.find_element_visible(ClaimsPageLocators.CONTROL_COMPLAINTS_SUMMARY_SELECTOR_DATE)
        assert element.is_displayed(), 'Селектор выбора периода динамики жалоб не отображен'

    @allure.title('Проверка селектора вкладок раздела "Жалобы"')
    @allure.description('Проверка смены вкладки при клике на таб селектора раздела "Жалобы"')
    def test_claims_summary_go_to_list(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        claims_page = ClaimsPage(browser)
        claims_page.go_to_claims_check_receipts()
        base_page = BasePage(browser)
        base_page.wait_element_visible(ClaimsPageLocators.CONTROL_COMPLAINTS_LIST)
        base_page.click_on_element(ClaimsPageLocators.CONTROL_COMPLAINTS_LIST)
        base_page.wait_element_visible(ClaimsPageLocators.CONTROL_COMPLAINTS_LIST_TABLE_COMPLAINTS)
        element = base_page.find_element_visible(ClaimsPageLocators.CONTROL_COMPLAINTS_LIST_TABLE_COMPLAINTS)
        assert element.is_displayed(), 'Переход во вкладку "Список" не осуществлен'


class TestClaimsList:

    @allure.title('Проверка фильтра списка жалоб')
    @allure.description('Проверка отображения панели фильтров списка жалоб')
    def test_claims_list_filter(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        claims_page = ClaimsPage(browser)
        claims_page.go_to_claims_check_receipts()
        base_page = BasePage(browser)
        element = base_page.find_element_visible(ClaimsPageLocators.CONTROL_COMPLAINTS_LIST_FILTER_PANEL)
        assert element.is_displayed(), 'Панель фильтрации жалоб не отображена'

    @allure.title('Проверка таблицы жалоб')
    @allure.description('Проверка отображения таблицы жалоб')
    def test_claims_list_table(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        claims_page = ClaimsPage(browser)
        claims_page.go_to_claims_check_receipts()
        base_page = BasePage(browser)
        base_page.wait_element_visible(ClaimsPageLocators.CONTROL_COMPLAINTS_LIST_TABLE_COMPLAINTS)
        element = base_page.find_element_visible(ClaimsPageLocators.CONTROL_COMPLAINTS_LIST_TABLE_COMPLAINTS)
        assert element.is_displayed(), 'Таблица жалоб не отображена'

    # @allure.title('Проверка шторки жалобы')
    # @allure.description('Проверка отображения шторки жалобы при клике на строку в таблице')
    # def test_claims_list_table_info(self, browser):
    #     authorization_page = AuthorizationPage(browser)
    #     authorization_page.get_authorization()
    #     claims_page = ClaimsPage(browser)
    #     claims_page.go_to_claims_check_receipts()
    #     base_page = BasePage(browser)
    #     base_page.click_on_element(ClaimsPageLocators.CONTROL_COMPLAINTS_LIST_CLAIM)
    #     time.sleep(3)
    #     assert len(base_page.find_element(ClaimsPageLocators.CONTROL_COMPLAINTS_LIST_SHTORKA_INFO_COMPLAINTS)) > 0, 'Элемент не найден'
