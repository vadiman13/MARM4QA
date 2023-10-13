from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators.locators
from data.urls import TestUrls
from data.creeds import VadlidCreeds, InvalidCreeds
from locators.locators import AuthorizationLocators, MapPageLocators, EconomicsPageLocators
import time
from pages.base_page import BasePage
from pages.authorization_page import AuthorizationPage
from pages.statistic_page import StatisticPage
from pages.economic_page import EconomicPage
from selenium.webdriver.common.by import By
import time
import allure
from data.elements import STATISTIC_ELEMENTS

# @allure.title('Проверка навигации по разделу "Экономика"')
# class TestEconomicSelector:
#     @allure.title('Проверка переключения подразделов')
#     @allure.description('Переключение таба выбора подраздела')
#     def test_switch_economic_tab(self, tab_name: str):
#         # pdb.set_trace()
#         tabs_element: Optional[WebElement] = self.find_element_visible(self.MAT_TAB_LINKS)
#
#         tab: Optional[WebElement] = tabs_element.find_element(By.XPATH, f".//*[contains(text(), '{tab_name}')]")
#
#         tab.click()
@allure.epic("Экономика")
@allure.feature('Тесты подраздела "ТЭК"')
class TestFuelPage:

    @allure.title('Проверка диаграммы "Общая выручка"')
    @allure.description(
        'Проверка видимости диаграммы "Общая выручка"')
    def test_check_fuel_cost_action_type_chart(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_fuel()
        element = economic_page.find_economic_element_visible(EconomicsPageLocators.ECONOMICS_TEC_TOTAL_COST_CHART)
        assert element.is_displayed(), 'Диаграмма "Общая выручка" не отображена'

    @allure.title('Проверка диаграммы "По типу налогообложения"')
    @allure.description('Проверка видимости диаграммы "По типу налогообложения"')
    def test_check_fuel_cost_taxation_chart(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_fuel()
        element = economic_page.find_economic_element_visible(EconomicsPageLocators.ECONOMICS_TEC_COST_TAXATION_CHART)
        assert element.is_displayed(), 'Диаграмма "По типу налогообложения" не отображена'


    @allure.title('Проверка графика "Средняя цена за литр"')
    @allure.description('Проверка видимости графика "Средняя цена за литр"')
    def test_check_fuel_avg_per_liter_chart(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_fuel()
        element = economic_page.find_economic_element_visible(EconomicsPageLocators.ECONOMICS_TEC_AVG_PER_LITER_CHART)
        assert element.is_displayed(), 'График "Средняя цена за литр" не отображен'


    @allure.title('Проверка селектора "Изменение даты статистики"')
    @allure.description('Проверка видимости селектора "Изменение даты статистики"')
    def test_check_fuel_range_selector(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_fuel()
        element = economic_page.find_economic_element_visible(EconomicsPageLocators.ECONOMICS_TEC_RANGE_SELECTOR)
        assert element.is_displayed(), 'Селектор "Изменение даты статистики" не отображен'


    @allure.title('Проверка графика "Общая выручка по типам топлива"')
    @allure.description('Проверка видимости графика "Общая выручка по типам топлива"')
    def test_check_cost_fuel_type_chart(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_fuel()
        element = economic_page.find_economic_element_visible(EconomicsPageLocators.ECONOMICS_TEC_COST_FUEL_TYPE_CHART)
        assert element.is_displayed(), 'График "Общая выручка по типам топлива" не отображен'


    @allure.title('Проверка графика "Общий литраж по типам топлива"')
    @allure.description('Проверка видимости графика "Общий литраж по типам топлива"')
    def test_check_volume_fuel_type_chart(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_fuel()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_TEC_VOLUME_FUEL_TYPE_CHART)
        assert element.is_displayed(), 'График "Общий литраж по типам топлива" не отображен'


    @allure.title('Проверка списка "ТОП 50 налогоплательщиков"')
    @allure.description('Проверка видимости списка "ТОП 50 налогоплательщиков"')
    def test_check_fuel_top_chart(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_fuel()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_TEC_TAXPAYERS_TOP_CHART)
        assert element.is_displayed(), 'Список "ТОП 50 налогоплательщиков" не отображен'

    @allure.title('Проверка тепловой карты средней цены по регионам')
    @allure.description('Проверка видимости тепловой карты средней цены по регионам')
    def test_check_fuel_map_chart(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_fuel()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_TEC_TAXPAYERS_TOP_CHART)
        assert element.is_displayed(), 'Тепловая карта средней цены по регионам не отображена'


@allure.epic("Экономика")
@allure.feature('Тесты подраздела "Индикаторы"')
class TestIndicatorsPage:
    @allure.title('Доля корзины в доходах: "ДОЛЯ ПРОДУКТОВОЙ КОРЗИНЫ В ДОХОДАХ НАСЕЛЕНИЯ"')
    @allure.description(
        'Проверка отображения диаграммы "ДОЛЯ ПРОДУКТОВОЙ КОРЗИНЫ В ДОХОДАХ НАСЕЛЕНИЯ"')
    def test_indicators_basket_proceeds_diagram_basket_proceeds(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_indicators_basket_proceeds()
        element = economic_page.find_economic_element_visible(EconomicsPageLocators.ECONOMICS_INDICATORS_BASKET_PROCEEDS_DIAGRAM_BASKET_PROCEEDS)
        assert element.is_displayed(), 'Диаграмма "ДОЛЯ ПРОДУКТОВОЙ КОРЗИНЫ В ДОХОДАХ НАСЕЛЕНИЯ" не отображена'

    @allure.title('Доля корзины в доходах: Тепловая карта регионов')
    @allure.description(
        'Проверка отображения Тепловой карты регионов')
    def test_indicators_basket_proceeds_map_basket_proceeds(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_indicators_basket_proceeds()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_INDICATORS_BASKET_PROCEEDS_MAP)
        assert element.is_displayed(), 'Тепловая карта регионов не отображена'

    @allure.title('Доля корзины в затратах: "ДОЛЯ ПРОДУКТОВОЙ КОРЗИНЫ В ОБЩИХ ЗАТРАТАХ НАСЕЛЕНИЯ"')
    @allure.description(
        'Проверка отображения диаграммы "ДОЛЯ ПРОДУКТОВОЙ КОРЗИНЫ В ОБЩИХ ЗАТРАТАХ НАСЕЛЕНИЯ"')
    def test_indicators_basket_proceeds_diagram_basket_proceeds(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_indicators_basket_cost()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_INDICATORS_BASKET_PROCEEDS_DIAGRAM_BASKET_PROCEEDS)
        assert element.is_displayed(), 'Диаграмма "ДОЛЯ ПРОДУКТОВОЙ КОРЗИНЫ В ОБЩИХ ЗАТРАТАХ НАСЕЛЕНИЯ" не отображена'

    @allure.title('Доля корзины в общих расходах: Тепловая карта регионов')
    @allure.description(
        'Проверка отображения Тепловой карты регионов')
    def test_indicators_basket_cost_map_basket_proceeds(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_indicators_basket_cost()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_INDICATORS_BASKET_COST_DIAGRAM_BASKET_COST)
        assert element.is_displayed(), 'Тепловая карта регионов не отображена'

    @allure.title('Доля продуктов питания: Диаграмма "Процент еды из общих затрат населения"')
    @allure.description('Проверка отображения диаграммы "Процент еды из общих затрат населения"')
    def test_indicators_food_diagram_food_cost_general(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_indicators_food()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_INDICATORS_FOOD_DIAGRAM_FOOD_COST_GENERAL)
        assert element.is_displayed(), 'Диаграмма "Процент еды из общих затрат населения" не отображена'

    @allure.title('Доля продуктов питания: Диаграмма "Затраты на еду на человека"')
    @allure.description('Проверка отображения диаграммы "Затраты на еду на человека"')
    def test_indicators_food_diagram_food_cost_human(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_indicators_food()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_INDICATORS_FOOD_DIAGRAM_FOOD_COST_HUMAN)
        assert element.is_displayed(), 'Диаграмма "Затраты на еду на человека" не отображена'

    @allure.title('Доля продуктов питания: Тепловая карта регионов')
    @allure.description('Проверка отображения Тепловой карты регионов')
    def test_indicators_food_map(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_indicators_food()
        element = economic_page.find_economic_element_visible(EconomicsPageLocators.ECONOMICS_INDICATORS_FOOD_MAP)
        assert element.is_displayed(), 'Тепловая карта регионов не отображена'

        assert element.is_displayed(), 'Селектор выбора даты предоставления статистики не отображен'

    @allure.title('Динамика стоимости корзины: Диаграмма "Статистика изменения цены по конкретным продуктам"')
    @allure.description('Проверка отображения диаграммы "Статистика изменения цены по конкретным продуктам"')
    def test_indicators_basket_dynamic_diagram_dynamic_price(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_indicators_basket_dynamic()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_INDICATORS_BASKET_DINAMYC_DIAGRAM_DYNAMIC_PRICE)
        assert element.is_displayed(), 'Диаграмма "Статистика изменения цены по конкретным продуктам" не отображена'

    @allure.title('Динамика стоимости корзины: Тепловая карта регионов')
    @allure.description('Проверка отображения Тепловой карты регионов')
    def test_indicators_basket_dynamic_map(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_indicators_basket_dynamic()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_INDICATORS_BASKET_DINAMYC_MAP)
        assert element.is_displayed(), 'Тепловая карта регионов не отображена'

    @allure.title('Доля алкоголя в затратах: Диаграмма "Доля алкоголя в общих затратах населения" (Выручка)')
    @allure.description('Проверка отображения диаграммы "Доля алкоголя в общих затратах населения" (Выручка)')
    def test_indicators_alcohol_cost_diagram_alcohol_cost_general(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_indicators_basket_alcohol_cost()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_INDICATORS_ALCOHOL_COST_DIAGRAM_ALCOHOL_COST_GENERAL)
        assert element.is_displayed()

    @allure.title('Доля алкоголя в затратах: Тепловая карта регионов (выручка)')
    @allure.description('Проверка отображения Тепловой карты регионов (выручка)')
    def test_indicators_alcohol_cost_map_proceeds(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_indicators_basket_alcohol_cost()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_INDICATORS_ALCOHOL_COST_MAP_PROCEEDS)
        assert element.is_displayed(), 'Тепловая карта регионов (выручка) не отображена'

    @allure.title('Доля алкоголя в затратах: Диаграмма "Доля алкоголя в общих затратах населения" (Литров в месяц)')
    @allure.description(
        'Проверка отображения диаграммы "Доля алкоголя в общих затратах населения" (Литров в месяц)')
    def test_indicators_alcohol_cost_diagram_alcohol_cost_human(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_indicators_basket_alcohol_cost()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_INDICATORS_ALCOHOL_COST_DIAGRAM_ALCOHOL_COST_HUMAN)
        assert element.is_displayed(), 'Диаграмма "Доля алкоголя в общих затратах населения" (Литров в месяц) не отображена'

    @allure.title('Доля алкоголя в затратах: Тепловая карта регионов (Литров в месяц)')
    @allure.description('Проверка отображения Тепловой карты регионов (Литров в месяц)')
    def test_indicators_alcohol_cost_map_liter(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_indicators_basket_alcohol_cost()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_INDICATORS_ALCOHOL_COST_MAP_LITER)
        assert element.is_displayed(), 'Тепловая карта регионов (Литров в месяц) не отображена'

    @allure.title(
        'Доля медикаментов в затратах: Диаграмма "Доля медикаментов в общих затратах населения" (Выручка)')
    @allure.description('Проверка отображения диаграммы "Доля медикаментов в общих затратах населения" (Выручка)')
    def test_indicators_medicine_cost_diagram_medicine_cost_general(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_indicators_basket_medicines_cost()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_INDICATORS_MEDICINE_COST_DIAGRAM_MEDICINE_COST_GENERAL)
        assert element.is_displayed(), 'Диаграмма "Доля медикаментов в общих затратах населения" (Выручка) не отображена'

    @allure.title('Доля медикаментов в затратах: Тепловая карта регионов (Выручка)')
    @allure.description('Проверка отображения Тепловой карты регионов (Выручка)')
    def test_indicators_medicine_cost_map_proceeds(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_indicators_basket_medicines_cost()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_INDICATORS_MEDICINE_COST_MAP_PROCEEDS)
        assert element.is_displayed(), 'Тепловая карта регионов (Выручка) не отображена'

    @allure.title(
        'Доля медикаментов в затратах: Диаграмма "Доля медикаментов в общих затратах населения" (Единиц в месяц)')
    @allure.description(
        'Проверка отображения диаграммы "Доля медикаментов в общих затратах населения" (Единиц в месяц)')
    def test_indicators_medicine_cost_diagram_medicine_cost_human(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_indicators_basket_medicines_cost()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_INDICATORS_MEDICINE_COST_DIAGRAM_MEDICINE_COST_HUMAN)
        assert element.is_displayed(), 'Диаграмма "Доля медикаментов в общих затратах населения" (Единиц в месяц) не отображена'

    @allure.title('Доля медикаментов в затратах: Тепловая карта регионов (Единиц в месяц)')
    @allure.description('Проверка отображения Тепловой карты регионов (Единиц в месяц)')
    def test_indicators_medicine_cost_map_unit(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_indicators_basket_medicines_cost()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_INDICATORS_MEDICINE_COST_MAP_UNIT)
        assert element.is_displayed(), 'Тепловая карта регионов (Единиц в месяц) не отображена'

    @allure.title('Доля табака в затратах: Диаграмма "Доля табачной продукции в общих затратах населения" (Выручка)')
    @allure.description('Проверка отображения диаграммы "Доля табачной продукции в общих затратах населения" (Выручка)')
    def test_indicators_tobacco_cost_diagram_tobacco_cost_general(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_indicators_basket_tobacco_cost()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_INDICATORS_TOBACCO_COST_DIAGRAM_TOBACCO_COST_GENERAL)
        assert element.is_displayed(), 'Диаграмма "Доля табачной продукции в общих затратах населения" (Выручка) не отображена'

    @allure.title('Доля табака в затратах: Тепловая карта выручки регионов')
    @allure.description('Проверка отображения Тепловой карты выручки регионов')
    def test_indicators_tobacco_cost_map_proceeds(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_indicators_basket_tobacco_cost()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_INDICATORS_TOBACCO_COST_MAP_PROCEEDS)
        assert element.is_displayed(), 'Тепловая карта выручки регионов не отображена'

    @allure.title(
        'Доля табака в затратах: Диаграмма "Доля табачной продукции в общих затратах населения" (Пачек в месяц)')
    @allure.description(
        'Проверка отображения диаграммы "Доля табачной продукции в общих затратах населения" (Пачек в месяц)')
    def test_indicators_tobacco_cost_diagram_tobacco_cost_human(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_indicators_basket_tobacco_cost()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_INDICATORS_TOBACCO_COST_DIAGRAM_TOBACCO_COST_HUMAN)
        assert element.is_displayed(), 'Диаграмма "Доля табачной продукции в общих затратах населения" (Пачек в месяц) не отображена'

    @allure.title('Доля табака в затратах: Тепловая карта объема потребления регионов')
    @allure.description('Проверка отображения Тепловой карты объема потребления регионов')
    def test_indicators_tobacco_cost_map_pack(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_indicators_basket_tobacco_cost()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_INDICATORS_TOBACCO_COST_MAP_PACK)
        assert element.is_displayed(), 'Тепловая карта объема потребления регионов не отображена'


@allure.epic("Экономика")
@allure.feature('Тесты подраздела "Розница"')
class TestRetailPage:
    @allure.title('Стоимость: Диаграмма СРЕДНЯЯ СТОИМОСТЬ ПРОДУКТОВОЙ КОРЗИНЫ ПО КАТЕГОРИЯМ')
    @allure.description('Проверка отображения диаграммы СРЕДНЯЯ СТОИМОСТЬ ПРОДУКТОВОЙ КОРЗИНЫ ПО КАТЕГОРИЯМ')
    def test_retail_totalcost_avg_categories_cost_chart(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_retail_total_cost()
        element = economic_page.find_economic_element_visible(EconomicsPageLocators.ECONOMICS_RETAIL_TOTAL_COST_AVG_CATEGORIES_COST_CHART)
        assert element.is_displayed(), 'Диаграмма "СРЕДНЯЯ СТОИМОСТЬ ПРОДУКТОВОЙ КОРЗИНЫ ПО КАТЕГОРИЯМ" не отображена'

    @allure.title('Стоимость: Селектор выбора даты статистики')
    @allure.description('Проверка отображения селектора выбора даты статистики')
    def test_retail_totalcost_date_range_selector(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_retail_total_cost()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_RETAIL_TOTAL_COST_DATE_RANGE_SELECTOR)
        assert element.is_displayed(), 'Селектор выбора даты статистики не отображен'

    @allure.title('Стоимость: График "Основные драйверы роста стоимости продуктовой корзины"')
    @allure.description('Проверка отображения графика "Основные драйверы роста стоимости продуктовой корзины"')
    def test_retail_totalcost_grow_drivers_chart(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_retail_total_cost()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_RETAIL_TOTAL_COST_GROW_DRIVERS_CHART)
        assert element.is_displayed(), 'График "Основные драйверы роста стоимости продуктовой корзины" не отображен'

    @allure.title('Стоимость: Тепловая карта')
    @allure.description('Проверка отображения тепловой карты')
    def test_retail_totalcost_map_area(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_retail_total_cost()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_RETAIL_TOTAL_COST_MAP_AREA)
        assert element.is_displayed(), 'Тепловая карта не отображена'

    @allure.title('Стоимость: График "Средняя стоимость продуктовой корзины по регионам"')
    @allure.description('Проверка отображения графика "Средняя стоимость продуктовой корзины по регионам"')
    def test_retail_totalcost_avg_regions_cost_chart(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_retail_total_cost()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_RETAIL_TOTAL_COST_AVG_REGIONS_COST_CHART)
        assert element.is_displayed(), 'График "Средняя стоимость продуктовой корзины по регионам" не отображен'

    @allure.title('Стоимость: Диаграмма "Товар по категориям"')
    @allure.description('Проверка отображения диаграммы "Товар по категориям"')
    def test_retail_totalcost_avg_categories_chart(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_retail_total_cost()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_RETAIL_TOTAL_COST_AVG_CATEGORIES_CHART)
        assert element.is_displayed(), 'Диаграмма "Товар по категориям" не отображена'

    @allure.title('Средняя цена: Диаграмма "Статистика изменения цены по категориям продуктов"')
    @allure.description('Проверка отображения диаграммы "Статистика изменения цены по категориям продуктов"')
    def test_retail_avg_price_chart(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_retail_avg_price()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_RETAIL_AVG_PRICE_AVG_PRICE_CHART)
        assert element.is_displayed(), 'Диаграмма "Статистика изменения цены по категориям продуктов" не отображена'

    @allure.title('Средняя цена: Селектор выбора даты статистики')
    @allure.description('Проверка отображения селектора выбора даты статистики')
    def test_retail_avg_price_date_range_selector(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_retail_avg_price()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_RETAIL_AVG_PRICE_DATE_RANGE_SELECTOR)
        assert element.is_displayed(), 'Селектор выбора даты статистики не отображен'

    @allure.title('Средняя цена: Диаграмма "Средняя цена по регионам"')
    @allure.description('Проверка отображения диаграммы "Средняя цена по регионам"')
    def test_retail_avg_price_avg_regions_cost_chart(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_retail_avg_price()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_RETAIL_AVG_PRICE_AVG_REGIONS_COST_CHART)
        assert element.is_displayed(), 'Диаграмма "Средняя цена по регионам" не отображена'


    @allure.title('Средняя цена: Тепловая карта регионов')
    @allure.description('Проверка отображения тепловой карты регионов')
    def test_retail_avg_price_map_area(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_retail_avg_price()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_RETAIL_AVG_PRICE_MAP_AREA)
        assert element.is_displayed(), 'Тепловая карта регионов не отображена'

    @allure.title('Объем потребления: Общий объём потребления выбранных категорий')
    @allure.description('Проверка отображения диаграммы "Общий объём потребления выбранных категорий"')
    def test_retail_consuming_avg_price_charting(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_retail_consuming()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_RETAIL_CONSUMING_AVG_PRICE_CHART)
        assert element.is_displayed(), 'Диаграмма "Общий объём потребления выбранных категорий"'

    @allure.title('Объем потребления: Селектор выбора даты статистики')
    @allure.description('Проверка отображения селектора выбора даты статистики')
    def test_retail_consuming_date_range(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_retail_consuming()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_RETAIL_CONSUMING_DATE_RANGE_SELECTOR)
        assert element.is_displayed(), 'Селектор выбора даты статистики не отображен'

    @allure.title('Объем потребления: Диаграмма "Объем потребления по регионам"')
    @allure.description('Проверка отображения диаграммы "Объем потребления по регионам"')
    def test_retail_consuming_avg_regions_cost_chart(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_retail_consuming()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_RETAIL_CONSUMING_AVG_REGIONS_COST_CHART)
        assert element.is_displayed(), 'Диаграмма "Объем потребления по регионам" не отображена'

    @allure.title('Объем потребления: Тепловая карта регионов')
    @allure.description('Проверка отображения тепловой карты регионов')
    def test_retail_consuming_map_area(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_retail_consuming()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_RETAIL_CONSUMING_MAP_AREA)
        assert element.is_displayed(), 'Тепловая карта регионов не отображена'

    @allure.title('Выручка: График "Общая выручка выбранных категорий"')
    @allure.description('Проверка отображения графика "Общая выручка выбранных категорий"')
    def test_retail_proceeds_avg_price_chart(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_retail_proceeds()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_RETAIL_PROCEEDS_AVG_PRICE_CHART)
        assert element.is_displayed(), 'График "Общая выручка выбранных категорий" не отображен'

    @allure.title('Выручка: Селектор выбора даты статистики')
    @allure.description('Проверка отображения селектора выбора даты статистики')
    def test_retail_proceeds_date_range(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_retail_proceeds()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_RETAIL_PROCEEDS_DATE_RANGE)
        assert element.is_displayed(), 'Селектор выбора даты статистики не отображен'

    @allure.title('Выручка: Диаграмма "Выручка по регионам"')
    @allure.description('Проверка отображения диаграммы "Выручка по регионам"')
    def test_retail_proceeds_avg_regions_cost_chart(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_retail_proceeds()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_RETAIL_PROCEEDS_AVG_REGIONS_COST_CHART)
        assert element.is_displayed(), 'Диаграмма "Выручка по регионам" не отображена'

    @allure.title('Выручка: Тепловая карта регионов')
    @allure.description('Проверка отображения тепловой карты регионов')
    def test_retail_proceeds_map_area(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_retail_proceeds()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_RETAIL_PROCEEDS_MAP_AREA)
        assert element.is_displayed(), 'Тепловая карта регионов не отображена'


@allure.epic("Экономика")
@allure.feature('Тесты подраздела "Анализ ТП"')
class TestTpAnalize:

    #Анализ ТП - таблица:
    @allure.title('Анализ ТП: Таблица')
    @allure.description('Проверка отображения таблицы анализа ТП')
    def test_analysis_tp_table(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_tp_analize()
        element = economic_page.find_economic_element_visible(EconomicsPageLocators.ECONOMICS_ANALYSIS_TP_SELECTOR)
        assert element.is_displayed(), 'Таблица анализа ТП не отображена'

    #Анализ ТП - древо категорий:

    @allure.title('Анализ ТП: Древо категорий')
    @allure.description('Проверка отображения древа категорий анализа ТП')
    def test_analysis_tp_drevo_categories(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_tp_analize()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_ANALYSIS_TP_DREVO_CATEGORIES)
        assert element.is_displayed(), 'Древо категорий анализа ТП не отображено'

    #Анализ ТП - диаграмма весов классификатора: **

    @allure.title('Анализ ТП: Диаграмма весов классификатора')
    @allure.description('Проверка отображения диаграммы весов классификатора анализа ТП')
    def test_analysis_tp_diagram_balance_classifier(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_tp_analize()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_ANALYSIS_TP_DIAGRAM_BALANCE_CLASSIFIER)
        assert element.is_displayed(), 'Диаграмма весов классификатора анализа ТП не отображена'

    # Анализ ТП - плашка со статистикой:

    @allure.title('Анализ ТП: Плашка со статистикой')
    @allure.description('Проверка отображения плашки со статистикой анализа ТП')
    def test_analysis_tp_table_statistic_bar(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        economic_page = EconomicPage(browser)
        economic_page.go_to_tp_analize()
        element = economic_page.find_economic_element_visible(
            EconomicsPageLocators.ECONOMICS_ANALYSIS_TP_TABLE_STATISTIC_BAR)
        assert element.is_displayed(), 'Плашка со статистикой анализа ТП не отображена'





















