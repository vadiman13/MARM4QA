from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators.locators
from data.urls import TestUrls
from data.creeds import VadlidCreeds, InvalidCreeds
from locators.locators import AuthorizationLocators, MapPageLocators, StatisticPageLocators
import time
from pages.base_page import BasePage
from pages.authorization_page import AuthorizationPage
from pages.statistic_page import StatisticPage
from selenium.webdriver.common.by import By
import time
import allure
from data.elements import STATISTIC_ELEMENTS


class TestStatisticPage:

    @allure.title("Проверка выпадающего календаря выбора диапазона дат")
    @allure.description(
        'Проверка видимости выпадающего календаря выбора диапазона дат')
    def test_check_cost_action_type_chart(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        statistic_page = StatisticPage(browser)
        statistic_page.go_to_statistic_main()
        element = statistic_page.find_statistic_element_visible(StatisticPageLocators.STATISTIC_DATE_RANGE_FILTER)
        assert element.is_displayed(), "Выпадающий календарь выбора диапазона дат не отображен"

    @allure.title("Проверка фильтра по ИНН")
    @allure.description(
        'Проверка видимости фильтра по ИНН')
    def test_check_cost_action_type_chart(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        statistic_page = StatisticPage(browser)
        statistic_page.go_to_statistic_main()
        element = statistic_page.find_statistic_element_visible(StatisticPageLocators.STATISTIC_INN_FILTER)
        assert element.is_displayed(), "Фильтр по ИНН не отображен"

    @allure.title("Проверка Диаграммы Выручка по видам деятельности")
    @allure.description(
        'Проверка видимости элемента "Диаграмма Выручка по видам деятельности" в видимой области экрана')
    def test_check_cost_action_type_chart(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        statistic_page = StatisticPage(browser)
        statistic_page.go_to_statistic_main()
        element = statistic_page.find_statistic_element_visible(StatisticPageLocators.STATISTIC_MAIN_COST_ACTION_TYPE_CHART)
        assert element.is_displayed(), "Диаграмма Выручка по видам деятельности не отображена"


    @allure.title("Проверка Диаграммы Выручка по типам налогообложения")
    @allure.description(
        'Проверка видимости элемента "Диаграмма Выручка по типам налогообложения" в видимой области экрана')
    def test_check_cost_taxation_chart(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        statistic_page = StatisticPage(browser)
        statistic_page.go_to_statistic_main()
        element = statistic_page.find_statistic_element_visible(StatisticPageLocators.STATISTIC_MAIN_COST_TAXATION_CHART)
        assert element.is_displayed(), "Диаграмма Выручка по типам налогообложения не отображена"


    @allure.title("Проверка Графика среднего чека")
    @allure.description('Проверка видимости элемента "График среднего чека" в видимой области экрана')
    def test_check_avg_check_chart(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        statistic_page = StatisticPage(browser)
        statistic_page.go_to_statistic_main()
        element = statistic_page.find_statistic_element_visible(StatisticPageLocators.STATISTIC_MAIN_AVG_CHECK_CHART)
        assert element.is_displayed(), "График среднего чека не отображен"


    @allure.title("Проверка Графика Общая выручка")
    @allure.description('Проверка видимости элемента "График Общая выручка" в видимой области экрана')
    def test_check_total_proceeds_chart(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        statistic_page = StatisticPage(browser)
        statistic_page.go_to_statistic_main()
        element = statistic_page.find_statistic_element_visible(StatisticPageLocators.STATISTIC_MAIN_TOTAL_PROCEEDS_CHART)
        assert element.is_displayed(), "График Общая выручка не отображен"


    @allure.title("Проверка ТОП 100 НП")
    @allure.description('Проверка видимости элемента "ТОП 100 НП" в видимой области экрана')
    def test_check_taxpayers_top_chart(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        statistic_page = StatisticPage(browser)
        statistic_page.go_to_statistic_main()
        element = statistic_page.find_statistic_element_visible(StatisticPageLocators.STATISTIC_MAIN_TAXPAYERS_TOP_CHART)
        assert element.is_displayed(), "ТОП 100 НП не отображен"

    @allure.title("Проверка ТОП 100 НП c отрицательной выручкой")
    @allure.description('Проверка видимости элемента "ТОП 100 НП c отрицательной выручкой" в видимой области экрана')
    def test_check_taxpayers_negative_top_chart(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        statistic_page = StatisticPage(browser)
        statistic_page.go_to_statistic_main()
        element = statistic_page.find_statistic_element_visible(StatisticPageLocators.STATISTIC_MAIN_TAXPAYERS_NEGATIVE_TOP_CHART)
        assert element.is_displayed(), "ТОП 100 НП c отрицательной выручкой не отображен"

    @allure.title("Проверка Тепловой карты регионов")
    @allure.description('Проверка видимости элемента "Тепловая карта регионов" в видимой области экрана')
    def test_check_statistic_regions_map(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        statistic_page = StatisticPage(browser)
        statistic_page.go_to_statistic_main()
        element = statistic_page.find_statistic_element_visible(StatisticPageLocators.STATISTIC_MAIN_REGIONS_MAP)
        assert element.is_displayed(), "Тепловая карта регионов не отображена"

    @allure.title("Проверка вкладки Геочеки")
    @allure.description('Проверка iframe "Геочеки"')
    def test_geochecs(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        statistic_page = StatisticPage(browser)
        statistic_page.go_to_statistic_geo()
        element = statistic_page.find_statistic_element_visible(StatisticPageLocators.STATISTIC_GEOCHEKI_IFRAME)
        assert element.is_displayed(), 'Окно "Геочеки" не отображено'








