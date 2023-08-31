from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators.locators
from data.urls import TestUrls
from data.creeds import VadlidCreeds, InvalidCreeds
from locators.locators import AuthorizationLocators, MapPageLocators, EconomicsPageLocators
import time
from pages.base_page import BasePage
from pages.authorization_page import AuthorizationPage
from selenium.webdriver.common.by import By
import time
import allure


@allure.title('Тесты на раздел "Экономика"')
class EconomicPage(BasePage):

    @allure.step('Переход в раздел "Экономика"')
    def go_to_fuel(self):
        self.go_to_page(TestUrls.EconomicsTecPageUrl)

    @allure.step('Проверка отображения элемента раздела статистика')
    def find_economic_element_visible(self, element, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(element))