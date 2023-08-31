from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators.locators
from data.urls import TestUrls
from data.creeds import VadlidCreeds, InvalidCreeds
from locators.locators import AuthorizationLocators, MapPageLocators, EconomicsPageLocators, ReportsPageLocators
import time
from pages.base_page import BasePage
from pages.reports_page import ReportsPage
from pages.authorization_page import AuthorizationPage
from selenium.webdriver.common.by import By
import time
import allure



class TestReportsPage:

    @allure.title('Проверка отчета "Страница отчетов"')
    @allure.description('Проверка видимости и активности элементов на странице отчетов')
    def test_selector_visible(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        reports_page = ReportsPage(browser)
        reports_page.go_to_reports()
        element = reports_page.find_reports_element_visible(ReportsPageLocators.REPORTS_MAT_TAB_LABELS)
        assert element.is_displayed(), 'Селектора переключения групп отчетов не отображен'

    @allure.title('Проверка активности табов')
    @allure.description('Проверка активности табов при переключении')
    def test_tab_activity(self, browser):
        authorization_page = AuthorizationPage(browser)
        authorization_page.get_authorization()
        reports_page = ReportsPage(browser)
        reports_page.go_to_reports()

        # Проверяем видимость селектора переключения групп отчетов
        element = reports_page.find_reports_elements_visible(ReportsPage.REPORTS_MAT_TAB_LABELS)
        assert element.is_displayed(), 'Селектор переключения групп отчетов не отображен'

        # Проверяем активность табов при переключении
        for i in range(6):
            reports_page.switch_tab(i)

            if i == 4:
                # Проверяем, что 5-й таб активен (выбран)
                assert reports_page.is_tab_active(i), f'Таб {i + 1} не активен'
            else:
                # Проверяем, что остальные табы не активны (не выбраны)
                assert not reports_page.is_tab_active(i), f'Таб {i + 1} активен, хотя не должен быть'
