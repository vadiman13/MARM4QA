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


class TestStatisticPage:

    #Поиск диаграммы по видам деятельности
    def test_check_statistic_cost_action_type(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        statistic_page = StatisticPage(browser)
        statistic_page.go_to_statistic_main()
        base_page = BasePage(browser)
        element = base_page.find_element_located(StatisticPageLocators.STATISTIC_MAIN_COST_ACTION_TYPE_CHART)
        assert element is not None, 'Диаграмма "Выручка по видам деятельности" не отображена'


