from selenium.webdriver.common.by import By

class AuthorizationLocators:
    LOGIN_INPUT = By.ID, "login"
    PASSWORD_INPUT = By.ID, "password"
    AUTH_BUTTON = By.XPATH, "//button[@type='submit']"
    ERROR = By.XPATH, '//p[contains(text(), "Ошибка. Вы ввели неверные авторизационные данные.")]'

class BasePageLocators:
    HEADER_MARM_LOGO = By.XPATH, ".//a[contains(@class, 'Header_LogoYandex__3TSOI')]"

class StatisticPageLocators:
    STATISTIC_MAIN_HEADER = By.XPATH, '//div[@class="page-header" and contains(text(), "Статистика")]' #Заголовок раздела "Статистика"
    STATISTIC_MAIN_COST_ACTION_TYPE_CHART = By.ID, 'cost-action-type-chart' #Диаграмма "Выручка по видам деятельности"
    STATISTIC_MAIN_COST_TAXATION_CHART = By.ID, 'cost-taxation-chart' #Диаграмма "Выручка по типам налогообложения"
    STATISTIC_MAIN_AVG_CHECK_CHART = By.ID, 'avg-check-chart' #График среднего чека
    STATISTIC_MAIN_TOTAL_PROCEEDS_CHART = By.ID, 'total-proceeds-chart'  #График "Общая выручка"
    STATISTIC_MAIN_TAXPAYERS_TOP_CHART = By.ID, 'taxpayers-top-chart'  #ТОП 100 НП
    STATISTIC_MAIN_TOTAL_NDS_DAY_CHART = By.ID, 'total-nds-day-chart'  #График общего НДС в день
    STATISTIC_MAIN_REGIONS_MAP = By.ID, 'regions-map'  #Тепловая карта регионов

class MapPageLocators:
    MAP = By.CLASS_NAME, "map-view"
