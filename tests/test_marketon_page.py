from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators.locators
from data.urls import TestUrls
from data.creeds import VadlidCreeds, InvalidCreeds
from locators.locators import AuthorizationLocators, MapPageLocators, EconomicsPageLocators, ReportsPageLocators, MarketonPageLocators
import time
from pages.base_page import BasePage
from pages.authorization_page import AuthorizationPage
from pages.marketon_page import MarketonPage
from pages.map_page import MapPage
from data.data import StatisticExpected
from selenium.webdriver.common.by import By
import time
import allure


@allure.epic("Контроль")
@allure.feature("Тесты подраздела Рынки")
class TestMarketon:

    # def test_check_fuel_cost_action_type_chart(self, browser):
    #     authorization_page = AuthorizationPage(browser)
    #     authorization_page.get_authorization()
    #     marketon_page = MarketonPage(browser)
    #     marketon_page.go_to_marketon()
    #
    # def test_marketon_table(self, browser):
    #     authorization_page = AuthorizationPage(browser)
    #     authorization_page.get_authorization()
    #     marketon_page = MarketonPage(browser)
    #     marketon_page.go_to_marketon()
    #     base_page = BasePage(browser)
    #     element = base_page.find_element_visible(MarketonPageLocators.MARKETON_TABLE)
    #     assert element.is_displayed(), 'Таблица рынков не отображена'

    def test_market_page(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        marketon_page = MarketonPage(browser)
        marketon_page.go_to_marketon()
        base_page = BasePage(browser)
        base_page.scroll_to(MarketonPageLocators.MARKET_EXAMPLE)
        base_page.click_on_element(MarketonPageLocators.MARKET_EXAMPLE)
        time.sleep(3)
