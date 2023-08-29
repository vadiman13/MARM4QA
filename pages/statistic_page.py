from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data.urls import TestUrls
from data.creeds import VadlidCreeds, InvalidCreeds
from locators.locators import AuthorizationLocators, MapPageLocators
import time
from pages.base_page import BasePage
from pages.authorization_page import VadlidCreeds
from selenium.webdriver.common.by import By
import time
import allure

class StatisticPage:

    @allure.step('Проверка ')
    def check_diagrams(self):
        self.go_to_autorization()
        self.valid_sign_marm()
        self.go_to_page(TestUrls.StatisticsMainPageUrl)

