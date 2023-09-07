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

class MapPage(BasePage):
    @allure.step('Получение кол-ва НП')
    def get_np(self):
        time.sleep(3)
        self.find_element(MapPageLocators.NP_STATISTIC).click
        element = self.find_element(MapPageLocators.NP_STATISTIC)
        text = element.text
        text = re.sub(r'\D', '', text)
        return text

    @allure.step('Получение кол-ва ККТ')
    def get_kkt(self):
        time.sleep(3)# Ждать до 10 секунд
        element = self.find_element(MapPageLocators.KKT_STATISTIC)
        text = element.text
        text = re.sub(r'\D', '', text)
        return text

    @allure.step('Клик на кнопку "Фильтры"')
    def filter_button_click(self):
        self.wait_element_visible(MapPageLocators.FILTERS_BUTTON)
        self.click_on_element(MapPageLocators.FILTERS_BUTTON)
        time.sleep(3)


    @allure.step('Поиск элемента')
    def find_map_element(self, element, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(element))


        # Сравнение чисел

