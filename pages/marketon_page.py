from typing import Optional

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators.locators
from data.urls import TestUrls
from data.creeds import VadlidCreeds, InvalidCreeds
from locators.locators import AuthorizationLocators, MapPageLocators, EconomicsPageLocators, ReportsPageLocators, MapPageLocators
import time
import re
from pages.base_page import BasePage
from pages.authorization_page import AuthorizationPage
from selenium.webdriver.common.by import By
import time
import allure

@allure.title('Тесты раздела "Рынки"')
class MarketonPage(BasePage):

    @allure.step('Переход в раздел "Рынки"')
    def go_to_marketon(self):
        self.go_to_page(TestUrls.ControlMarketPageUrl)
        time.sleep(3)



