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


class TestCases:
    @allure.title('ТК')
    @allure.description('Проверка перехода в карточку НП')
    def test_tc_one(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()