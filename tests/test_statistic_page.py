from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data.urls import TestUrls
from data.creeds import VadlidCreeds, InvalidCreeds
from locators.locators import AuthorizationLocators, MapPageLocators
import time
from pages.base_page import BasePage
from pages.statistic_page import StatisticPage
from selenium.webdriver.common.by import By
import time
import allure


class TestStatisticPage:
    def test_check_statistic(self, browser):
        statistic_page = StatisticPage(browser)
        statistic_page.go_to_statistic_main()
        time.sleep(3)

