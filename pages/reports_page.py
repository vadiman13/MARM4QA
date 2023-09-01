from typing import Optional

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators.locators
from data.urls import TestUrls
from data.creeds import VadlidCreeds, InvalidCreeds
from locators.locators import AuthorizationLocators, MapPageLocators, EconomicsPageLocators, ReportsPageLocators
import time
from pages.base_page import BasePage
from pages.authorization_page import AuthorizationPage
from selenium.webdriver.common.by import By
import time
import allure

import pdb

class ReportsPage(BasePage):
    REPORTS_MAT_TAB_LABELS = By.CLASS_NAME, "mat-tab-labels"

    @allure.step('Переход в раздел "Отчеты"')
    def go_to_reports(self):
        self.go_to_page(TestUrls.ReportsPageUrl)

    @allure.step('Проверка отображения элемента раздела отчетов')
    def find_reports_element_visible(self, element, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(element))

    @allure.step('Проверка отображения элементов раздела отчетов')
    def find_reports_elements_visible(self, element, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(element))

    @allure.step('Переключение таба')
    def switch_tab(self, tab_name: str):
        # pdb.set_trace()
        tabs_element: Optional[WebElement] = self.find_reports_elements_visible(self.REPORTS_MAT_TAB_LABELS)

        tab: Optional[WebElement] = tabs_element.find_element(By.XPATH, f".//*[contains(text(), '{tab_name}')]")

        tab.click()

    @allure.step('Проверка активности таба')
    def is_tab_active(self, index):
        tabs = self.find_reports_elements_visible(self.REPORTS_MAT_TAB_LABELS)
        return tabs[index].get_attribute('aria-selected') == 'true'