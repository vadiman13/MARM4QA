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

@allure.title('Тесты раздела "Жалобы"')
class ClaimsPage(BasePage):
    @allure.step('Переход в раздел "Жалобы-Сводка"')
    def go_to_claims_summary(self):
        self.go_to_page(TestUrls.ControlCivilClaimsSummaryPageUrl)
        time.sleep(3)

    @allure.step('Переход в раздел "Жалобы-Список"')
    def go_to_claims_check_receipts(self):
        self.go_to_page(TestUrls.ControlCivilClaimsListPageUrl)
        time.sleep(3)