from selenium.webdriver.common.by import By

class AuthorizationLocators:
    LOGIN_INPUT = By.ID, "login"
    PASSWORD_INPUT = By.ID, "password"
    AUTH_BUTTON = By.XPATH, "//button[@type='submit']"
    ERROR = By.XPATH, '//p[contains(text(), "Ошибка. Вы ввели неверные авторизационные данные.")]'
    AUTHORIZATION_FORM = By.XPATH, '//div[contains(@class, "sc-fKFyDc")]'

class BasePageLocators:
    HEADER_MARM_LOGO = By.XPATH, ".//a[contains(@class, 'Header_LogoYandex__3TSOI')]"
    LOGOUT_BUTTON = By.XPATH, "//button[text()='Выйти']"


class ReportsPageLocators: #Отчеты
    REPORTS_HEADER = By.CLASS_NAME, 'title'  #Заголовок раздела "Отчеты", неуникальный локатор
    REPORTS_MAT_TAB_LABELS = By.XPATH, "//div[@class='mat-tab-labels']"  #Селектор выбора категории отчетов
    REPORTS_MENU_ITEM = By.XPATH, "//li[contains(@class, 'navigation_') and contains(@class, 'ng-star-inserted')]"  #Пункт меню "Отчеты"

class StatisticPageLocators:
    STATISTIC_MAIN_HEADER = By.XPATH, '//div[@class="page-header" and contains(text(), "Статистика")]' #Заголовок раздела "Статистика"
    STATISTIC_MAIN_COST_ACTION_TYPE_CHART = By.ID, 'cost-action-type-chart' #Диаграмма "Выручка по видам деятельности"
    STATISTIC_MAIN_COST_TAXATION_CHART = By.ID, 'cost-taxation-chart' #Диаграмма "Выручка по типам налогообложения"
    STATISTIC_MAIN_AVG_CHECK_CHART = By.ID, 'avg-check-chart' #График среднего чека
    STATISTIC_MAIN_TOTAL_PROCEEDS_CHART = By.ID, 'total-proceeds-chart'  #График "Общая выручка"
    STATISTIC_MAIN_TAXPAYERS_TOP_CHART = By.ID, 'taxpayers-top-chart'  #ТОП 100 НП
    STATISTIC_MAIN_TAXPAYERS_NEGATIVE_TOP_CHART = By.ID, 'taxpayers-negative-top-chart'  # ТОП 100 НП с отрицательной выручкой
    STATISTIC_MAIN_TOTAL_NDS_DAY_CHART = By.ID, 'total-nds-day-chart'  #График общего НДС в день
    STATISTIC_MAIN_REGIONS_MAP = By.ID, 'regions-map'  #Тепловая карта регионов
    STATISTIC_DATE_RANGE_FILTER = By.CLASS_NAME, 'date-range-filter'
    STATISTIC_INN_FILTER = By.CLASS_NAME, 'inn_filter'
    STATISTIC_GEOCHEKI_IFRAME = By.XPATH, '//iframe[@src="https://geochecki-vpd.nalog.gov.ru/#/geochecks"]'  # Окно геочеков

class MapPageLocators:
    MAP = By.CLASS_NAME, "map-view"
    NP_STATISTIC = By.XPATH, "//*[text()=' Налогоплательщики ']/following-sibling::div"
    KKT_STATISTIC = By.XPATH, "//*[text()='ККТ']/following-sibling::div"
    FILTERS_BUTTON = By.XPATH, '//app-filters-button[contains(@class, "button")]'
    FILTERS_FORM = By.XPATH, '//p[contains(@class, "title") and text()="Настройки отображения на карте"]'
    ASK_KKT_LOGO = By.CLASS_NAME, 'logo-title-block'
    SEARCH_INPUT = By.XPATH, '//*[@placeholder="Поиск по НП, ККТ, торговым точкам и объектам"]'
    SEARCH_BUTTON = By.XPATH, '//span[@class="icon icon-input-search-white"]'
    SEARCH_NP_BUTTON = By.XPATH, '//span[contains(text(), "НП")]'
    SEARCH_NP_TEST_RESULT = By.XPATH, '//header[@class="item__text ng-star-inserted" and text()="7724490000 АО ПОЧТА РОССИИ"]'
    SEARCH_NP_TEST_CARD_BUTTON = By.XPATH, '//a[starts-with(@class, "link") and contains(@href, "/marm/map-clean/card/taxpayer/7724490000")]'
    SEARCH_NP_TEST_CARD_HEADER = By.XPATH, '//div[contains(@class, "card-breadcrumbs__item") and contains(text(), "7724490000 - АО ПОЧТА РОССИИ (Почта России)")]'


class EconomicsPageLocators: #Экономика

    #ТЭК
    ECONOMICS_TEC_TOTAL_COST_CHART = By.ID, 'total-cost-chart'  #Диаграмма "Общая выручка"
    ECONOMICS_TEC_COST_TAXATION_CHART = By.ID, 'cost-taxation-chart'  #Диаграмма "По типу налогооблажения"
    ECONOMICS_TEC_AVG_PER_LITER_CHART = By.ID, 'avg-per-liter-chart'  #График средней цены за литр (график)
    ECONOMICS_TEC_RANGE_SELECTOR = By.ID, 'range-selector'  #Селектор изменения даты статистики, неуникальный локатор
    ECONOMICS_TEC_COST_FUEL_TYPE_CHART = By.ID, 'cost-fuel-type-chart'  #График общей выручки по типам топлива
    ECONOMICS_TEC_VOLUME_FUEL_TYPE_CHART = By.ID, 'volume-fuel-type-chart'  #График общего литража по типам топлива
    ECONOMICS_TEC_REGIONS_MAP = By.ID, 'regions-map'  #Тепловая карта
    ECONOMICS_TEC_TAXPAYERS_TOP_CHART = By.ID, 'taxpayers-top-chart'  #ТОП 50 НП, неуникальный локатор

    #Розница
    #Стоимость

    ECONOMICS_RETAIL_TOTAL_COST_AVG_CATEGORIES_COST_CHART = By.ID, 'avg-categories-cost-chart'  #График "Средняя стоимость продуктовой корзины по категориям" (consumerbasketprice)
    ECONOMICS_RETAIL_TOTAL_COST_DATE_RANGE_SELECTOR = By.ID, 'date-range-selector'  #Селектор выбора даты статистики
    ECONOMICS_RETAIL_TOTAL_COST_GROW_DRIVERS_CHART = By.ID, 'grow-drivers-chart'  #График "Основные драйверы роста стоимости продуктовой корзины" (consumerbasketpricedriver)
    ECONOMICS_RETAIL_TOTAL_COST_MAP_AREA = By.ID, 'map-area'  #Тепловая карта (consbasketavgregionprice)
    ECONOMICS_RETAIL_TOTAL_COST_AVG_REGIONS_COST_CHART = By.ID, 'avg-regions-cost-chart'  #График "Средняя стоимость продуктовой корзины по регионам" (consbasketavgregionprice)
    ECONOMICS_RETAIL_TOTAL_COST_AVG_CATEGORIES_CHART = By.ID, 'avg-categories-chart'  #Диаграмма "Товар по категориям" (consbasketcategoriesregion)

    #Средняя цена

    ECONOMICS_RETAIL_AVG_PRICE_AVG_PRICE_CHART = By.ID, 'avg-price-chart'  #График Статистика изменения цены по категориям продуктов (consumerbasketstatistic)
    ECONOMICS_RETAIL_AVG_PRICE_DATE_RANGE_SELECTOR = By.ID, 'date-range-selector' #Селектор выбора даты статистики
    ECONOMICS_RETAIL_AVG_PRICE_AVG_REGIONS_COST_CHART = By.ID, 'avg-regions-cost-chart'  #Диаграмма "Средняя цена по регионам" (consbasketavgpriceregion), локатор неуникальный
    ECONOMICS_RETAIL_AVG_PRICE_MAP_AREA = By.ID, 'map-area'  #Тепловая карта регионов (consbasketavgpriceregion)

    #Объем потребления

    ECONOMICS_RETAIL_CONSUMING_AVG_PRICE_CHART = By.ID, 'avg-price-chart'  #График "Общий объём потребления выбранных категорий" (consumerbasketstatistic)
    ECONOMICS_RETAIL_CONSUMING_DATE_RANGE_SELECTOR = By.ID, 'date-range-selector'  #Селектор выбора даты статистики
    ECONOMICS_RETAIL_CONSUMING_AVG_REGIONS_COST_CHART = By.ID, 'avg-regions-cost-chart'  #Диаграмма "Объём потребления по регионам" (consbasketavgpriceregion), локатор неуникальный
    ECONOMICS_RETAIL_CONSUMING_MAP_AREA = By.ID, 'map-area'  #Тепловая карта регионов (consbasketavgpriceregion)

    #Выручка

    ECONOMICS_RETAIL_PROCEEDS_AVG_PRICE_CHART = By.ID, 'avg-price-chart'  #График "Общая выручка выбранных категорий" (consumerbasketstatistic)
    ECONOMICS_RETAIL_PROCEEDS_DATE_RANGE = By.ID, 'date-range-selector'  #Селектор выбора даты статистики
    ECONOMICS_RETAIL_PROCEEDS_AVG_REGIONS_COST_CHART = By.ID, 'avg-regions-cost-chart'  #Диаграмма "Выручка по регионам" (consbasketavgpriceregion)
    ECONOMICS_RETAIL_PROCEEDS_MAP_AREA = By.ID, 'map-area'  #Тепловая карта регионов (consbasketavgpriceregion)

    #Анализ чеков

    ECONOMICS_RETAIL_CHECK_ANALYSIS_SELECTOR = By.XPATH, '//div[contains(@class, "col-md-4") and contains(@class, "view-page-links")]' #Селектор вкладок
    ECONOMICS_RETAIL_CHECK_DREVO_CATEGORIES = By.XPATH, '//div[contains(@class, "categories-tree") and contains(@class, "col-lg-3")]'  #Древо категорий

    #Анализ чеков - таблица

    ECONOMICS_RETAIL_CHECK_TABLE_STATISTIC_BAR = By.CLASS_NAME, 'statistic-bar'  #Плашка со статистикой, неуникальный селектор

    #Анализ чеков - диаграмма - объем потребления

    ECONOMICS_RETAIL_CHECK_DIAGRAM_CONSUMPTION_DYNAMICS_CONSUMPTION = By.ID, 'diagram3'  #График динамики потребления, неуникальный селектор
    ECONOMICS_RETAIL_CHECK_DIAGRAM_CONSUMPTION_DIAGRAM_SUBCATEGORY = By.ID, 'diagram'  #Диаграмма Подкатегорий, неуникальный селектор
    ECONOMICS_RETAIL_CHECK_DIAGRAM_CONSUMPTION_DIAGRAM_MONTH = By.ID, 'diagram-radar'  #Диаграмма По месяцам

    #Анализ чеков - диаграмма - выручка

    ECONOMICS_RETAIL_CHECK_DIAGRAM_PROCEEDS_DIAGRAM_DYNAMICS_CONSUMPTION = By.ID, 'diagram3'  #График динамики потребления
    ECONOMICS_RETAIL_CHECK_DIAGRAM_PROCEEDS_DIAGRAM_SUBCATEGORY = By.ID, 'diagram'  #Диаграмма Подкатегорий, неуникальный селектор
    ECONOMICS_RETAIL_CHECK_DIAGRAM_PROCEEDS_DIAGRAM_MONTH = By.ID, 'diagram-radar'  #Диаграмма По месяцам

    #Анализ чеков - диаграмма - средняя цена

    ECONOMICS_RETAIL_CHECK_DIAGRAM_AVG_PRICE_DIAGRAM_DYNAMICS_CONSUMPTION = By.ID, 'diagram3'  #График динамики потребления
    ECONOMICS_RETAIL_CHECK_DIAGRAM_AVG_PRICE_DIAGRAM_SUBCATEGORY = By.ID, 'diagram'  #Диаграмма Подкатегорий, неуникальный селектор
    ECONOMICS_RETAIL_CHECK_DIAGRAM_AVG_PRICE_DIAGRAM_MONTH = By.ID, 'diagram-radar'  #Диаграмма По месяцам

    #Анализ чеков - карта - объем потребления

    ECONOMICS_RETAIL_CHECK_MAP_CONSUMPTION_MAP_AREA = By.ID, 'map-area'  #Тепловая карта
    ECONOMICS_RETAIL_CHECK_MAP_CONSUMPTION_DIAGRAM_REGIONS = By.ID, 'diagram'  #Диаграмма со списком регионов, неуникальный селектор
    ECONOMICS_RETAIL_CHECK_MAP_CONSUMPTION_BUTTON_CALENDAR = By.XPATH, "//button[contains(@class, 'mat-icon-button') and @aria-label='Open calendar']"  #Кнопка открытия календаря
    ECONOMICS_RETAIL_CHECK_MAP_CONSUMPTION_CALENDAR = By.XPATH, "//*[starts-with(@id, 'cdk-overlay-')]"  #Календарь

    #Анализ чеков - карта - выручка

    ECONOMICS_RETAIL_CHECK_MAP_PROCEEDS_MAP_AREA = By.ID, 'map-area'  #Тепловая карта
    ECONOMICS_RETAIL_CHECK_MAP_PROCEEDS_DIAGRAM_REGIONS = By.ID, 'diagram'  #Диаграмма со списком регионов, неуникальный селектор
    ECONOMICS_RETAIL_CHECK_MAP_PROCEEDS_BUTTON_CALENDAR = By.XPATH, "//button[contains(@class, 'mat-icon-button') and @aria-label='Open calendar']"  #Кнопка открытия календаря
    ECONOMICS_RETAIL_CHECK_MAP_PROCEEDS_CALENDAR = By.XPATH, "//*[starts-with(@id, 'cdk-overlay-')]"  #Календарь

    #Анализ чеков - карта - средняя цена

    ECONOMICS_RETAIL_CHECK_MAP_AVG_PRICE_MAP_AREA = By.ID, 'map-area'  # Тепловая карта
    ECONOMICS_RETAIL_CHECK_MAP_AVG_PRICE_DIAGRAM_REGIONS = By.ID, 'diagram'  #Диаграмма со списком регионов, неуникальный селектор
    ECONOMICS_RETAIL_CHECK_MAP_AVG_PRICE_BUTTON_CALENDAR = By.XPATH, "//button[contains(@class, 'mat-icon-button') and @aria-label='Open calendar']"  #Кнопка открытия календаря
    ECONOMICS_RETAIL_CHECK_MAP_AVG_PRICE_CALENDAR = By.XPATH, "//*[starts-with(@id, 'cdk-overlay-')]"  #Календарь

    #Анализ ТП - таблица

    ECONOMICS_ANALYSIS_TP_SELECTOR = By.XPATH, '//div[contains(@class, "col-md-4") and contains(@class, "view-page-links")]'  #Селектор вкладок
    ECONOMICS_ANALYSIS_TP_DREVO_CATEGORIES = By.XPATH, '//div[contains(@class, "categories-tree") and contains(@class, "col-lg-3")]'  #Древо категорий
    ECONOMICS_ANALYSIS_TP_DIAGRAM_BALANCE_CLASSIFIER = By.XPATH, "//div[@id='words-network']"  #Диаграмма весов классификатора, !элемент не найден
    ECONOMICS_ANALYSIS_TP_TABLE_STATISTIC_BAR = By.CLASS_NAME, "statistic-bar"  #Плашка со статистикой, неуникальный селектор

    #Анализ ТП - диаграмма - объем потребления

    ECONOMICS_ANALYSIS_TP_DIAGRAM_CONSUMPTION_DIAGRAM_DYNAMICS_CONSUMPTION = By.ID, 'diagram3'  #График динамики потребления
    ECONOMICS_ANALYSIS_TP_DIAGRAM_CONSUMPTION_DIAGRAM_SUBCATEGORY = By.ID, 'diagram'  #Диаграмма Подкатегорий, неуникальный селектор
    ECONOMICS_ANALYSIS_TP_DIAGRAM_CONSUMPTION_DIAGRAM_MONTH = By.ID, 'diagram-radar'  #Диаграмма По месяцам
    ECONOMICS_ANALYSIS_TP_DIAGRAM_CONSUMPTION_BUTTON_CALENDAR = By.XPATH, "//button[contains(@class, 'mat-icon-button') and @aria-label='Open calendar']"  #Кнопка открытия календаря
    ECONOMICS_ANALYSIS_TP_DIAGRAM_CONSUMPTION_CALENDAR = By.ID, 'mat-dialog-0'  #Календарь

    #Анализ ТП - диаграмма - выручка

    ECONOMICS_ANALYSIS_TP_DIAGRAM_PROCEEDS_DIAGRAM_DYNAMICS_CONSUMPTION = By.ID, 'diagram3'  #График динамики потребления
    ECONOMICS_ANALYSIS_TP_DIAGRAM_PROCEEDS_DIAGRAM_SUBCATEGORY = By.ID, 'diagram'  #Диаграмма Подкатегорий, неуникальный селектор
    ECONOMICS_ANALYSIS_TP_DIAGRAM_PROCEEDS_DIAGRAM_MONTH = By.ID, 'diagram-radar'  #Диаграмма По месяцам
    ECONOMICS_ANALYSIS_TP_DIAGRAM_PROCEEDS_BUTTON_CALENDAR = By.XPATH, "//button[contains(@class, 'mat-icon-button') and @aria-label='Open calendar']"  #Кнопка открытия календаря
    #НЕ ХВАТАЕТ КАЛЕНДАРЯ

    #Анализ ТП - диаграмма - средняя цена

    ECONOMICS_ANALYSIS_TP_DIAGRAM_AVG_PRICE_DIAGRAM_DYNAMICS_CONSUMPTION = By.ID, 'diagram3'  #График динамики потребления
    ECONOMICS_ANALYSIS_TP_DIAGRAM_AVG_PRICE_DIAGRAM_SUBCATEGORY = By.ID, 'diagram'  #Диаграмма Подкатегорий, неуникальный селектор
    ECONOMICS_ANALYSIS_TP_DIAGRAM_AVG_PRICE_DIAGRAM_MONTH = By.ID, 'diagram-radar'  #Диаграмма По месяцам
    # НЕ ХВАТАЕТ КНОПКИ ОТКРЫТИЯ КАЛЕНДАРЯ
    # НЕ ХВАТАЕТ КАЛЕНДАРЯ

    #Анализ ТП - карта - объем потребления

    ECONOMICS_ANALYSIS_TP_SELECTOR = By.ID, 'diagramType'  #Селектор вкладок подраздела
    ECONOMICS_ANALYSIS_TP_MAP_CONSUMPTION_MAP_AREA = By.ID, 'map-area'  #Тепловая карта
    ECONOMICS_ANALYSIS_TP_MAP_CONSUMPTION_DIAGRAM_REGIONS = By.ID, 'diagram'  #Диаграмма со списком регионов, неуникальный селектор
    ECONOMICS_ANALYSIS_TP_MAP_CONSUMPTION_BUTTON_CALENDAR = By.XPATH, "//button[contains(@class, 'mat-icon-button') and @aria-label='Open calendar']"  #Кнопка открытия календаря
    ECONOMICS_ANALYSIS_TP_MAP_CONSUMPTION_CALENDAR = By.XPATH, "//*[starts-with(@id, 'cdk-overlay-')]"  #Календарь

    #Анализ ТП - карта - выручка

    ECONOMICS_ANALYSIS_TP_MAP_PROCEEDS_MAP_AREA = By.ID, 'map-area'  #Тепловая карта
    ECONOMICS_ANALYSIS_TP_MAP_PROCEEDS_DIAGRAM_REGIONS = By.ID, 'diagram'  #Диаграмма со списком регионов, неуникальный селектор
    # НЕ ХВАТАЕТ КНОПКИ ОТКРЫТИЯ КАЛЕНДАРЯ
    # НЕ ХВАТАЕТ КАЛЕНДАРЯ

    #Анализ ТП - карта - средняя цена

    ECONOMICS_ANALYSIS_TP_MAP_AVG_PRICE_MAP_AREA = By.ID, 'map-area'  #Тепловая карта
    ECONOMICS_ANALYSIS_TP_MAP_AVG_PRICE_DIAGRAM_REGIONS = By.ID, 'diagram'  #Диаграмма со списком регионов, неуникальный селектор
    # НЕ ХВАТАЕТ КНОПКИ ОТКРЫТИЯ КАЛЕНДАРЯ
    # НЕ ХВАТАЕТ КАЛЕНДАРЯ

    #Индикаторы - доля корзины в доходах

    ECONOMICS_INDICATORS_BASKET_PROCEEDS_DIAGRAM_BASKET_PROCEEDS = By.CLASS_NAME, 'dx-visibility-change-handler'  #Диаграмма "Доля продуктовой корзины в доходах населения
    ECONOMICS_INDICATORS_BASKET_PROCEEDS_MAP = By.CSS_SELECTOR, '[id*="area"]'  #Тепловая карта регионов

    #Индикаторы - доля корзины в затратах

    ECONOMICS_INDICATORS_BASKET_COST_DIAGRAM_BASKET_COST = By.CLASS_NAME, "dx-visibility-change-handler"  #График "Доля продуктовой корзины в затратах населения"
    ECONOMICS_INDICATORS_BASKET_COST_MAP = By.CSS_SELECTOR, '[id*="area"]'  #Тепловая карта регионов

    #Индикаторы - доля продуктов питания

    ECONOMICS_INDICATORS_FOOD_DIAGRAM_FOOD_COST_GENERAL = By.ID, "food-population-percentage"  #Диаграмма "Процент еды из общих затрат населения", неуникальный локатор
    ECONOMICS_INDICATORS_FOOD_DIAGRAM_FOOD_COST_HUMAN = By.ID, "food-costs-per-capita"  #Диаграмма "Затраты на еду на человека, неуникальный локатор
    ECONOMICS_INDICATORS_FOOD_MAP = By.CSS_SELECTOR, '[id*="area"]'  #Тепловая карта регионов

    #Индикаторы - динамика стоимости корзины

    ECONOMICS_INDICATORS_BASKET_DINAMYC_DIAGRAM_BASKET_DYNAMIC = By.CLASS_NAME, 'dx-visibility-change-handler'  #Диаграмма "Динамика изменения стоимости продуктовой корзины", неуникальный локатор
    ECONOMICS_INDICATORS_BASKET_DINAMYC_SELECTOR = By.ID, 'range-selector'  #Селектор выбора даты предоставления статистики, неуникальный локатор
    ECONOMICS_INDICATORS_BASKET_DINAMYC_DIAGRAM_DYNAMIC_PRICE = By.CLASS_NAME, 'basket-products-chart'  #Диаграмма "Статистика изменения цены по конкретным продуктам"
    ECONOMICS_INDICATORS_BASKET_DINAMYC_MAP = By.CSS_SELECTOR, '[id*="area"]'  #Тепловая карта регионов

    #Индикаторы - доля алкоголя в затратах

    ECONOMICS_INDICATORS_ALCOHOL_COST_DIAGRAM_ALCOHOL_COST_GENERAL = By.CLASS_NAME, 'dx-visibility-change-handler'  #Диаграмма "Доля алкоголя в общих затратах населения" (Выручка), неуникальный локатор
    ECONOMICS_INDICATORS_ALCOHOL_COST_MAP_PROCEEDS = By.CSS_SELECTOR, '[id*="area"]'  #Тепловая карта регионов (выручка), неуникальный локатор
    ECONOMICS_INDICATORS_ALCOHOL_COST_DIAGRAM_ALCOHOL_COST_HUMAN = By.CLASS_NAME, 'dx-visibility-change-handler'  #Диаграмма "Доля алкоголя в общих затратах населения" (Литров в месяц), неуникальный локатор
    ECONOMICS_INDICATORS_ALCOHOL_COST_MAP_LITER = By.CSS_SELECTOR, '[id*="area"]'  #Тепловая карта регионов (Литров в месяц), неуникальный локатор

    #Индикаторы - доля медикаментов в затратах

    ECONOMICS_INDICATORS_MEDICINE_COST_DIAGRAM_MEDICINE_COST_GENERAL = By.CLASS_NAME, 'dx-visibility-change-handler'  #Диаграмма "Доля медикаментов в общих затратах населения" (Выручка), неуникальный локатор
    ECONOMICS_INDICATORS_MEDICINE_COST_MAP_PROCEEDS = By.CSS_SELECTOR, '[id*="area"]'  #Тепловая карта выручки регионов (Выручка), неуникальный локатор
    ECONOMICS_INDICATORS_MEDICINE_COST_DIAGRAM_MEDICINE_COST_HUMAN = By.CLASS_NAME, 'dx-visibility-change-handler'  #Диаграмма "Доля медикаментов в общих затратах населения" (Единиц в месяц), неуникальный локатор
    ECONOMICS_INDICATORS_MEDICINE_COST_MAP_UNIT = By.CSS_SELECTOR, '[id*="area"]'  #Тепловая карта выручки регионов (Единиц в месяц), неуникальный локатор

    #Индикаторы - доля табака в затратах

    ECONOMICS_INDICATORS_TOBACCO_COST_DIAGRAM_TOBACCO_COST_GENERAL = By.CLASS_NAME, 'dx-visibility-change-handler' #Диаграмма "Доля табачной продукции в общих затратах населения" (Выручка), неуникальный локатор
    ECONOMICS_INDICATORS_TOBACCO_COST_MAP_PROCEEDS = By.CSS_SELECTOR, '[id*="area"]'  #Тепловая карта выручки регионов, неуникальный локатор
    ECONOMICS_INDICATORS_TOBACCO_COST_DIAGRAM_TOBACCO_COST_HUMAN = By.CLASS_NAME, 'dx-visibility-change-handler'  #Диаграмма "Доля табачной продукции в общих затратах населения" (Пачек в месяц), неуникальный локатор
    ECONOMICS_INDICATORS_TOBACCO_COST_MAP_PACK = By.CSS_SELECTOR, '[id*="area"]'  #Тепловая карта объема потребления регионов, неуникальный локатор

    #Анализ ТП - таблица

    ECONOMICS_ANALYSIS_TP_SELECTOR = By.XPATH, '//div[contains(@class, "col-md-4") and contains(@class, "view-page-links")]'  #Селектор вкладок
    ECONOMICS_ANALYSIS_TP_DREVO_CATEGORIES = By.XPATH, '//div[contains(@class, "categories-tree") and contains(@class, "col-lg-3")]'  #Древо категорий
    ECONOMICS_ANALYSIS_TP_DIAGRAM_BALANCE_CLASSIFIER = By.XPATH, "//div[@id='words-network']"  #Диаграмма весов классификатора, !элемент не найден
    ECONOMICS_ANALYSIS_TP_TABLE_STATISTIC_BAR = By.CLASS_NAME, "statistic-bar"  #Плашка со статистикой, неуникальный селектор

class MarketonPageLocators:

    MARKETON_TABLE = By.XPATH, '//div[@class="table"]'
    MARKET_EXAMPLE = By.XPATH, "//a[text()='ОРПЦ \"ФУД СИТИ\"']"

class ClaimsPageLocators:
    CONTROL_COMPLAINTS_SUMMARY_DIAGRAM_STATISTIC_COMPLAINTS = By.CLASS_NAME, "summary-charts"  # Диаграммы статистики жалоб, неуникальный локатор
    CONTROL_COMPLAINTS_SUMMARY_DIAGRAM_DYNAMICS_COMPLAINTS = By.CLASS_NAME, "dynamics-body"  # Диаграмма динамики жалоб, неуникальный локатор
    CONTROL_COMPLAINTS_SUMMARY_SELECTOR_DATE = By.CSS_SELECTOR, ".claims-dynamics-filter-form.ng-untouched.ng-pristine.ng-valid"  # Селектор дат ДОЛЖЕН БЫТЬ ВЫПАДАЮЩИЙ КАЛЕНДАРЬ?

    # Список
    CONTROL_COMPLAINTS_LIST = By.XPATH, "//*[contains(@class,'mat-tab-link') and contains(text(),'Список')]"  # Переход к списку жалоб
    CONTROL_COMPLAINTS_LIST_CLAIM = By.XPATH, "//td[@class='mat-cell cdk-cell cdk-column-DateClaim mat-column-DateClaim ng-star-inserted']"
    CONTROL_COMPLAINTS_LIST_FILTER_PANEL = By.CSS_SELECTOR, "form.filter-form.ng-untouched.ng-pristine.ng-valid"  # Панель фильтрации жалоб
    CONTROL_COMPLAINTS_LIST_TABLE_COMPLAINTS = By.CLASS_NAME, "claims-table"  # Таблица жалоб, неуникальный локатор
    CONTROL_COMPLAINTS_LIST_TABLE_FILTER_PANEL_ = By.CSS_SELECTOR, ".mat-row.cdk-row.ng-star-inserted"  # Панель фильтрации жалоб, неуникальный локатор
    CONTROL_COMPLAINTS_LIST_SHTORKA_INFO_COMPLAINTS = By.XPATH, '//div[@class="general-info show fixed"]'
        #By.CSS_SELECTOR, "div.general-info.show.fixed"  # Шторка инфо о жалобе, неуникальный локатор

class AutonomusPageLocators:
    #Автономные территории
    CONTROL_AUTONOMOUS_HEADER = By.XPATH, "//div[@class='heading' and contains(text(), ' Автономные территории ')]"  #Заголовок страницы
    CONTROL_AUTONOMOUS_BUTTON_ADD_AT = By.CSS_SELECTOR, "button.button.button-img.add-btn.ng-star-inserted"  #Кнопка добавления АТ
    CONTROL_AUTONOMOUS_FILTERS_PANEL = By.CLASS_NAME, "regulatory-documents-filter"  #Панель фильтров, неуникальный локатор
    CONTROL_AUTONOMOUS_BUTTON_RESET_FILTER = By.CSS_SELECTOR, "button.button-reset"  #Кнопка сброса фильтров, неуникальный локатор
    CONTROL_AUTONOMOUS_BUTTON_UNLOADING_LOGS = By.CSS_SELECTOR, "button.button-img.button-primary.ng-star-inserted"  #Кнопка выгрузки логов
    CONTROL_AUTONOMOUS_TABLE_AT = By.CLASS_NAME, "table-container"  #Таблица АТ, неуникальный локатор
    CONTROL_AUTONOMOUS_CARD_TREE = By.CLASS_NAME, "tree"
    CONTROL_AUTONOMOUS_CARD_TEST = By.XPATH, '//td[@class="mat-cell cdk-cell clickable cdk-column-region mat-column-region ng-star-inserted"][normalize-space()="01 - Республика Адыгея"]'
    CONTROL_AUTONOMOUS_CARD_AT = By.CSS_SELECTOR, "td.mat-cell.cdk-cell.clickable.cdk-column-region.mat-column-region.ng-star-inserted"  #Карточка АТ, неуникальный локатор
    CONTROL_AUTONOMOUS_HEADER_REGION = By.CLASS_NAME, "heading"  #Шапка с наименование региона, неуникальный локатор