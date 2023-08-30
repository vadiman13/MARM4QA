from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import locators.locators
from data.urls import TestUrls
from data.creeds import VadlidCreeds, InvalidCreeds
from locators.locators import AuthorizationLocators, MapPageLocators
import time
from pages.base_page import BasePage
from pages.authorization_page import VadlidCreeds
from selenium.webdriver.common.by import By
import time
import allure

class StatisticPage(BasePage):

    @allure.step('Переход в раздел Статистика-Основная')
    def go_to_statistic_main(self):
        self.get_authorization()
        self.go_to_page(TestUrls.StatisticsMainPageUrl)







