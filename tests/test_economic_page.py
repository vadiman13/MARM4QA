from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators.locators
from data.urls import TestUrls
from data.creeds import VadlidCreeds, InvalidCreeds
from locators.locators import AuthorizationLocators, MapPageLocators, EconomicsPageLocators
import time
from pages.base_page import BasePage
from pages.authorization_page import AuthorizationPage
from pages.statistic_page import StatisticPage
from pages.economic_page import EconomicPage
from selenium.webdriver.common.by import By
import time
import allure
from data.elements import STATISTIC_ELEMENTS

@allure.title('Тесты подраздела "ТЭК"')
class TestFuelPage:

    @allure.title('Проверка диаграммы "Общая выручка"')
    @allure.description(
        'Проверка видимости диаграммы "Общая выручка"')
    def test_check_fuel_cost_action_type_chart(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_fuel()
        element = economic_page.find_economic_element_visible(EconomicsPageLocators.ECONOMICS_TEC_TOTAL_COST_CHART)
        assert element.is_displayed(), 'Диаграмма "Общая выручка" не отображена'

    @allure.title('Проверка диаграммы "По типу налогообложения"')
    @allure.description('Проверка видимости диаграммы "По типу налогообложения"')
    def test_check_fuel_cost_taxation_chart(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_fuel()
        element = economic_page.find_economic_element_visible(EconomicsPageLocators.ECONOMICS_TEC_COST_TAXATION_CHART)
        assert element.is_displayed(), 'Диаграмма "По типу налогообложения" не отображена'


    @allure.title('Проверка графика "Средняя цена за литр"')
    @allure.description('Проверка видимости графика "Средняя цена за литр"')
    def test_check_fuel_avg_per_liter_chart(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_fuel()
        element = economic_page.find_economic_element_visible(EconomicsPageLocators.ECONOMICS_TEC_AVG_PER_LITER_CHART)
        assert element.is_displayed(), 'График "Средняя цена за литр" не отображен'


    @allure.title('Проверка селектора "Изменение даты статистики"')
    @allure.description('Проверка видимости селектора "Изменение даты статистики"')
    def test_check_fuel_range_selector(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_fuel()
        element = economic_page.find_economic_element_visible(EconomicsPageLocators.ECONOMICS_TEC_RANGE_SELECTOR)
        assert element.is_displayed(), 'Селектор "Изменение даты статистики" не отображен'


    @allure.title('Проверка графика "Общая выручка по типам топлива"')
    @allure.description('Проверка видимости графика "Общая выручка по типам топлива"')
    def test_check_cost_fuel_type_chart(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_fuel()
        element = economic_page.find_economic_element_visible(EconomicsPageLocators.ECONOMICS_TEC_COST_FUEL_TYPE_CHART)
        assert element.is_displayed(), 'График "Общая выручка по типам топлива" не отображен'


    @allure.title('Проверка графика "Общий литраж по типам топлива"')
    @allure.description('Проверка видимости графика "Общий литраж по типам топлива"')
    def test_check_volume_fuel_type_chart(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_fuel()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_TEC_VOLUME_FUEL_TYPE_CHART)
        assert element.is_displayed(), 'График "Общий литраж по типам топлива" не отображен'


    @allure.title('Проверка списка "ТОП 50 налогоплательщиков"')
    @allure.description('Проверка видимости списка "ТОП 50 налогоплательщиков"')
    def test_check_fuel_top_chart(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_fuel()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_TEC_TAXPAYERS_TOP_CHART)
        assert element.is_displayed(), 'Список "ТОП 50 налогоплательщиков" не отображен'

    @allure.title('Проверка тепловой карты средней цены по регионам')
    @allure.description('Проверка видимости тепловой карты средней цены по регионам')
    def test_check_fuel_map_chart(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_fuel()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_TEC_TAXPAYERS_TOP_CHART)
        assert element.is_displayed(), 'Тепловая карта средней цены по регионам не отображена'


class TestFuelPage:

