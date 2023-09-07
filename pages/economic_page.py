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

    @allure.step('Переход в раздел "Экономика" - "ТЭК"')
    def go_to_fuel(self):
        self.go_to_page(TestUrls.EconomicsTecPageUrl)

    @allure.step('Переход в раздел "Индикаторы" - "Доля корзины в доходах"')
    def go_to_indicators_basket_proceeds(self):
        self.go_to_page(TestUrls.EconomicsIndicatorsBasketProceedsPageUrl)

    @allure.step('Переход в раздел "Индикаторы" - "Доля корзины в затратах"')
    def go_to_indicators_basket_cost(self):
        self.go_to_page(TestUrls.EconomicsIndicatorsBasketCostPageUrl)

    @allure.step('Переход в раздел "Индикаторы" - "Доля продуктов питания"')
    def go_to_indicators_food(self):
        self.go_to_page(TestUrls.EconomicsIndicatorsFoodPageUrl)

    @allure.step('Переход в раздел "Индикаторы" - "Динамика стоимости корзины"')
    def go_to_indicators_basket_dynamic(self):
        self.go_to_page(TestUrls.EconomicsIndicatorsBasketDynamicPageUrl)

    @allure.step('Переход в раздел "Индикаторы" - "Доля алкоголя в затратах"')
    def go_to_indicators_basket_alcohol_cost(self):
        self.go_to_page(TestUrls.EconomicsIndicatorsAlcoholCostPageUrl)

    @allure.step('Переход в раздел "Индикаторы" - "Доля медикаментов в затратах"')
    def go_to_indicators_basket_medicines_cost(self):
        self.go_to_page(TestUrls.EconomicsIndicatorsMedicineCostPageUrl)

    @allure.step('Переход в раздел "Индикаторы" - "Доля табака в затратах"')
    def go_to_indicators_basket_tobacco_cost(self):
        self.go_to_page(TestUrls.EconomicsIndicatorsTobaccoCostPageUrl)

    @allure.step('Переход в раздел "Розница" - "Стоимость"')
    def go_to_retail_total_cost(self):
        self.go_to_page(TestUrls.EconomicsRetailTotalCostPageUrl)

    @allure.step('Переход в раздел "Розница" - "Средняя стоимость"')
    def go_to_retail_avg_price(self):
        self.go_to_page(TestUrls.EconomicsRetailAvgPricePageUrl)

    @allure.step('Переход в раздел "Розница" - "Объем потребления"')
    def go_to_retail_consuming(self):
        self.go_to_page(TestUrls.EconomicsRetailConsumptionPageUrl)

    @allure.step('Переход в раздел "Розница" - "Выручка"')
    def go_to_retail_proceeds(self):
        self.go_to_page(TestUrls.EconomicsRetailProceedsPageUrl)

    @allure.step('Переход в раздел "Анализ ТП" - таблица')
    def go_to_tp_analize(self):
        self.go_to_page(TestUrls.EconomicsTPAnalizeTable)

    @allure.step('Проверка отображения элемента раздела статистика')
    def find_economic_element_visible(self, element, time=40):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(element))