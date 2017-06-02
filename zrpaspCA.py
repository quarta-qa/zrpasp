from pages import *
from setup import *


class TestSuite:

    @classmethod
    def setup_class(cls):
        """
        Тут описывается что происходит ПЕРЕД запуском всех тестов.
        Сейчас тут описан драйвер, а также подготовка окна браузера и
        переход на нужную ссылку.
        """
        cls.driver = webdriver.Chrome("C:\Python34\Scripts\chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.get(Links.main_page)

    @classmethod
    def teardown_class(cls):
        """
        Тут описывается что происходит ПОСЛЕ запуском всех тестов.
        Сейчас тут просто убивается драйвер после прогона.
        """
        cls.driver.quit()

    def test_login(self):
        """
        Любой тест должен начинаться с test_
        """
        data = load_data("logpas")

        p = LoginPage(self.driver)
        p.username(data["username"])
        p.password(data["password"])
        p.lot()
        p.click_by_name("Войти")

    # Расчет итогов
    def test_resultcalculation(self):

        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["calculation"])
        n.click_menu_section(data["menu"]["secondLevel"]["resultСalculation"])
        n.find_error()

    # Расчет синтетики
    def test_calculationsynthetics(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["calculation"])
        n.click_menu_section(data["menu"]["secondLevel"]["calculationSynthetics"])
        n.find_error()

    # Расчет аналитики
    def test_calculationanalytics(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["calculation"])
        n.click_menu_section(data["menu"]["secondLevel"]["calculationAnalytics"])
        n.find_error()

    # Закрытие расчетного периода Зарплата
    def test_closuresalary(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["calculation"])
        n.click_menu_section(data["menu"]["secondLevel"]["closureSalary"])
        n.find_error()

    # Закрытие расчетного периода Аналитика
    def test_closureanalytics(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["calculation"])
        n.click_menu_section(data["menu"]["secondLevel"]["ClosureAnalytics"])
        n.find_error()

    # Восстановление ЕСН
    def test_restoreesn(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["calculation"])
        n.click_menu_section(data["menu"]["secondLevel"]["RestoreESN"])
        n.find_error()

    # Перенос долга сотрудников
    def test_transfereployees(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["calculation"])
        n.click_menu_section(data["menu"]["secondLevel"]["TransferEployees"])
        n.find_error()

    # Поэтапный расчет аналитики-Расчет кредита
    def test_calculationcredit(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["calculation"])
        n.click_menu_section(data["menu"]["secondLevel"]["PhasedPaymentAnalytics"])
        n.click_menu_section(data["menu"]["thirdLevel"]["calculationCredit"])
        n.find_error()

    # Поэтапный расчет аналитики-Расчет дебета
    def test_calculation_debit(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["calculation"])
        n.click_menu_section(data["menu"]["secondLevel"]["PhasedPaymentAnalytics"])
        n.click_menu_section(data["menu"]["thirdLevel"]["calculationDebit"])
        n.find_error()

    # Поэтапный расчет аналитики-Расчет начислений
    def test_calculation_charges(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["calculation"])
        n.click_menu_section(data["menu"]["secondLevel"]["PhasedPaymentAnalytics"])
        n.click_menu_section(data["menu"]["thirdLevel"]["calculationCharges"])
        n.find_error()

    # Окончательный расчет проводок
    def test_final_payment_transactions(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["calculation"])
        n.click_menu_section(data["menu"]["secondLevel"]["FinalPaymentTransactions"])
        n.find_error()

    # Предварительный расчет проводок
    def test_calculation_transactions(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["calculation"])
        n.click_menu_section(data["menu"]["secondLevel"]["calculationTransactions"])
        n.find_error()

    # Резерв отпусков
    def test_reserveholidays(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["calculation"])
        n.click_menu_section(data["menu"]["secondLevel"]["ReserveHolidays"])
        n.find_error()

    # Расчет даты выплаты последней МП/ЕВ
    def test_calculationpayment_mp_eb(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["calculation"])
        n.click_menu_section(data["menu"]["secondLevel"]["calculationPaymentMP_EB"])
        n.find_error()

    # Проверка данных для аналитики
    def test_checking_analytics(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["calculation"])
        n.click_menu_section(data["menu"]["secondLevel"]["checkingAnalytics"])
        n.find_error()

    # Экспорт в кадры
    def test_export_frames(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["calculation"])
        n.click_menu_section(data["menu"]["secondLevel"]["ExportFrames"])
        n.find_error()

    # Импорт из кадров-Реестр загруженных файлов
    def test_registryfilesdownloaded(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["calculation"])
        n.click_menu_section(data["menu"]["secondLevel"]["ImportsFrames"])
        n.click_menu_section(data["menu"]["thirdLevel"]["RegistryFilesDownloaded"])
        n.find_error()

    # Журнал документов
    def test_documentjournal(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["documentJournal"])
        n.find_error()

    # Оформление документов
    def test_paperwork(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["Paperwork"])
        n.find_error()

    # Журнал проводок
    def test_journalentries(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["journalEntries"])
        n.find_error()

    # Структура подразделений
    def test_structure(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["structure"])
        n.find_error()

    # Штатное расписание
    def test_staff(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["staff"])
        n.find_error()

    # Платежные ведомости
    def test_payrolls(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["payrolls"])
        n.find_error()

    # Депоненты
    def test_depositors(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["Depositors"])
        n.find_error()

    # Расходные ордера
    def test_withdrawal(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["withdrawal"])
        n.find_error()

    # Исполнительные листы
    def test_enforcementorders(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["EnforcementOrders"])
        n.find_error()

    # инвалиды
    def test_peopledisabilities(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["PeopleDisabilities"])
        n.find_error()

    # Пенсионный фонд-Анкетные данные
    def test_personaldata(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["PensionFund"])
        n.click_menu_section(data["menu"]["thirdLevel"]["PersonalData"])
        n.find_error()

    # Пенсионный фонд-Сведения
    def test_intelligence(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["PensionFund"])
        n.click_menu_section(data["menu"]["thirdLevel"]["Intelligence"])
        n.find_error()

    # Пенсионный фонд-Пачки РСВ-1
    def test_bundlesrsv_1(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["PensionFund"])
        n.click_menu_section(data["menu"]["thirdLevel"]["BundlesRSV_1"])
        n.find_error()

    # Пенсионный фонд-Пачки СПВ-1,2,СЗВ-6-1,2,4 и РСВ-1(ИС) и СЗВ-М
    def test_bundlesspvbcr(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["PensionFund"])
        n.click_menu_section(data["menu"]["thirdLevel"]["BundlesSPVBCR"])
        n.find_error()

    # Пенсионный фонд-Дополнительная настройка расчета ПФ
    def test_additional_configuration_pf_calculation(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["PensionFund"])
        n.click_menu_section(data["menu"]["thirdLevel"]["AdditionalconfigurationPFcalculation"])
        n.find_error()

    # Пенсионный фонд-Задвоенные сотрудники
    def test_zadvoennye_employees(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["PensionFund"])
        n.click_menu_section(data["menu"]["thirdLevel"]["ZadvoennyeEmployees"])
        n.find_error()

    # Пенсионный фонд-Заявление ДСВ-1
    def test_statementbydsv_1(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["PensionFund"])
        n.click_menu_section(data["menu"]["thirdLevel"]["StatementbyDSV_1"])
        n.find_error()

    # Пенсионный фонд-Реестр ДСВ-3
    def test_registrydsv_3(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["PensionFund"])
        n.click_menu_section(data["menu"]["thirdLevel"]["RegistryDSV_3"])
        n.find_error()

    # Журнал отпусков / больничных
    def test_journalholiday(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["journalHoliday"])
        n.find_error()

    # Отчет в ГНИ -Сбор сведений о доходах, вычетах, налогах за год
    def test_gatheringinformation(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["ReportSGNI"])
        n.click_menu_section(data["menu"]["thirdLevel"]["GatheringInformation"])
        n.find_error()

    #  Отчет в ГНИ -Просмотр собранных данных
    def test_viewingthecollecteddata(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["ReportSGNI"])
        n.click_menu_section(data["menu"]["thirdLevel"]["ViewingtheCollectedData"])
        n.find_error()

    # Отчет в ГНИ - Сбор сведений о доходах, вычетах, налогах  6-НДФЛ
    def test_gatheringinformationdeductions(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["ReportSGNI"])
        n.click_menu_section(data["menu"]["thirdLevel"]["GatheringInformationDeductions"])
        n.find_error()

    # Отчет в ГНИ - Просмотр собранных данных для 6-НДФЛ
    def test_viewingcollecteddata6ndfl(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["ReportSGNI"])
        n.click_menu_section(data["menu"]["thirdLevel"]["VieWingCollectedData6NDFL"])
        n.find_error()

    # Формирование ПП во внебюджетные- Настройка получателей ПП в фондах
    def test_recipientconfigurationppfunds(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["FormationPPiVV"])
        n.click_menu_section(data["menu"]["thirdLevel"]["RecipientConfigurationPPFunds"])
        n.find_error()

    # Формирование ПП во внебюд- Настройка получателей ПП в регионах
    def test_recipient_configuration_regions(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["FormationPPiVV"])
        n.click_menu_section(data["menu"]["thirdLevel"]["RecipientConfigurationPPRegions"])
        n.find_error()

    # Формирование ПП во внебюд- Формирование ПП
    def test_formationpp(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["FormationPPiVV"])
        n.click_menu_section(data["menu"]["thirdLevel"]["formationPP"])
        n.find_error()

    # Формирование итоговых ПП по НДФЛ
    def test_formation_pppttt(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["FormationAllPPPIT"])
        n.find_error()

    # Платежные ведомости из кассы
    def test_payrolls_cash(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["PayrollsCash"])
        n.find_error()

    # Оборотная ведомость
    def test_backved(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["settings"])
        n.click_menu_section(data["menu"]["secondLevel"]["BackVED"])
        n.find_error()

    # Справочники-Балансовые счета
    def test_balance_sheet_accounts(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["references"])
        n.click_menu_section(data["menu"]["secondLevel"]["BalanceSheetAccounts"])
        n.find_error()

    # Справочники-Типовые операции
    def test_typical_operations(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["references"])
        n.click_menu_section(data["menu"]["secondLevel"]["TypicalOperations"])
        n.find_error()

    # Справочники-Сотрудники
    def test_eployees(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["references"])
        n.click_menu_section(data["menu"]["secondLevel"]["Employees"])
        n.find_error()

    # Справочники-Информация об организации
    def test_information_organization(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["references"])
        n.click_menu_section(data["menu"]["secondLevel"]["InformationOrganization"])
        n.find_error()

    # Справочники-Виды финансирования
    def test_types_financing(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["references"])
        n.click_menu_section(data["menu"]["secondLevel"]["TypesFinancing"])
        n.find_error()

    # Справочники-Элементы затрат
    def test_cost_elements(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["references"])
        n.click_menu_section(data["menu"]["secondLevel"]["costElements"])
        n.find_error()

    # Справочники-Календарь
    def test_calendar(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["references"])
        n.click_menu_section(data["menu"]["secondLevel"]["calendar"])
        n.find_error()

    # Справочники-Группа балансовых счетов
    def test_group_balance_accounts(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["references"])
        n.click_menu_section(data["menu"]["secondLevel"]["GroupBalanceAccounts"])
        n.find_error()

    # Справочники-ЗАРПЛАТА-Фонд рабочего времени
    def test_fund_working_time(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["references"])
        n.click_menu_section(data["menu"]["secondLevel"]["SALARY"])
        n.click_menu_section(data["menu"]["thirdLevel"]["FundWorkingTime"])
        n.find_error()

    # Справочники-ЗАРПЛАТА-Классификатор вычетов
    def test_qualifier_deductions(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["references"])
        n.click_menu_section(data["menu"]["secondLevel"]["SALARY"])
        n.click_menu_section(data["menu"]["thirdLevel"]["Qualifierdeductions"])
        n.find_error()

    # Справочники-ЗАРПЛАТА-Классификатор доходов
    def test_qua_lifierin_come(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["references"])
        n.click_menu_section(data["menu"]["secondLevel"]["SALARY"])
        n.click_menu_section(data["menu"]["thirdLevel"]["Qualifierincome"])
        n.find_error()

    # Справочники-ЗАРПЛАТА-Справочник начислений
    def test_referen_cecharges(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["references"])
        n.click_menu_section(data["menu"]["secondLevel"]["SALARY"])
        n.click_menu_section(data["menu"]["thirdLevel"]["Referencecharges"])
        n.find_error()

    # Справочники-ЗАРПЛАТА-Справочник удержаний
    def test_referencedeductions(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["references"])
        n.click_menu_section(data["menu"]["secondLevel"]["SALARY"])
        n.click_menu_section(data["menu"]["thirdLevel"]["Referencedeductions"])
        n.find_error()

    # Справочники-ЗАРПЛАТА-Категории учета рабочего времени
    def test_categories_working_time(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["references"])
        n.click_menu_section(data["menu"]["secondLevel"]["SALARY"])
        n.click_menu_section(data["menu"]["thirdLevel"]["CategoriesWorkingTime"])
        n.find_error()

    # Справочники-ЗАРПЛАТА-Шкала налоговой таблицы подоходного налога
    def test_scaletax_table_cometax(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["references"])
        n.click_menu_section(data["menu"]["secondLevel"]["SALARY"])
        n.click_menu_section(data["menu"]["thirdLevel"]["TheScaleTaxTableinCometax"])
        n.find_error()

    # Справочники-ЗАРПЛАТА-Справочник ведомостей
    def test_statements_directory(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["references"])
        n.click_menu_section(data["menu"]["secondLevel"]["SALARY"])
        n.click_menu_section(data["menu"]["thirdLevel"]["statementsDirectory"])
        n.find_error()

    # Справочники-ЗАРПЛАТА-Справочник должностей
    def test_guide_posts(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["references"])
        n.click_menu_section(data["menu"]["secondLevel"]["SALARY"])
        n.click_menu_section(data["menu"]["thirdLevel"]["Guideposts"])
        n.find_error()

    # Справочники-ЗАРПЛАТА-Справочник групп должностей
    def test_guide_posts_groups(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["references"])
        n.click_menu_section(data["menu"]["secondLevel"]["SALARY"])
        n.click_menu_section(data["menu"]["thirdLevel"]["Guidepostsgroups"])
        n.find_error()

    # Справочники-ЗАРПЛАТА-Справочник подразделений
    def test_referen_ceunits(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["references"])
        n.click_menu_section(data["menu"]["secondLevel"]["SALARY"])
        n.click_menu_section(data["menu"]["thirdLevel"]["ReferenCeunits"])
        n.find_error()

    # Справочники-ЗАРПЛАТА-Затраты для аналитики
    def test_costs_analysts(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["references"])
        n.click_menu_section(data["menu"]["secondLevel"]["SALARY"])
        n.click_menu_section(data["menu"]["thirdLevel"]["CostsAnalysts"])
        n.find_error()

    # Справочники-ЗАРПЛАТА-Начисления на зарплату
    def test_accruals_wages(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["references"])
        n.click_menu_section(data["menu"]["secondLevel"]["SALARY"])
        n.click_menu_section(data["menu"]["thirdLevel"]["Accrualsforwages"])
        n.find_error()

    # Справочники-ЗАРПЛАТА-Отчисления
    def test_royalties(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["references"])
        n.click_menu_section(data["menu"]["secondLevel"]["SALARY"])
        n.click_menu_section(data["menu"]["thirdLevel"]["royalties"])
        n.find_error()

    # Справочники-ЗАРПЛАТА-Справочник групп начислений
    def test_directory_accrual_groups(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["references"])
        n.click_menu_section(data["menu"]["secondLevel"]["SALARY"])
        n.click_menu_section(data["menu"]["thirdLevel"]["Directoryaccrualgroups"])
        n.find_error()

    # Справочники-ЗАРПЛАТА-Почтовые сборы
    def test_postage(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["references"])
        n.click_menu_section(data["menu"]["secondLevel"]["SALARY"])
        n.click_menu_section(data["menu"]["thirdLevel"]["postage"])
        n.find_error()

    # Справочники-ЗАРПЛАТА-Категории работников по затратам
    def test_categories_workers_costs(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["references"])
        n.click_menu_section(data["menu"]["secondLevel"]["SALARY"])
        n.click_menu_section(data["menu"]["thirdLevel"]["CategoriesWorkersCosts"])
        n.find_error()

    # Справочники-ЗАРПЛАТА-Шкала страховых взносов
    def test_scale_premiums(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["references"])
        n.click_menu_section(data["menu"]["secondLevel"]["SALARY"])
        n.click_menu_section(data["menu"]["thirdLevel"]["ThescalePremiums"])
        n.find_error()

    # Справочники-ЗАРПЛАТА-Типы оплаты
    def test_payment_types(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["references"])
        n.click_menu_section(data["menu"]["secondLevel"]["SALARY"])
        n.click_menu_section(data["menu"]["thirdLevel"]["paymentTypes"])
        n.find_error()

    # Справочники-ЗАРПЛАТА-Классификатор \"Выслуга лет- основание
    def test_qualifier_base(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["references"])
        n.click_menu_section(data["menu"]["secondLevel"]["SALARY"])
        n.click_menu_section(data["menu"]["thirdLevel"]["QualifierBase"])
        n.find_error()

    # Справочники-ЗАРПЛАТА-Таблица соответствий ставок и часов
    def test_table_rate_sand_hours(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["references"])
        n.click_menu_section(data["menu"]["secondLevel"]["SALARY"])
        n.click_menu_section(data["menu"]["thirdLevel"]["TableOfratesandhours"])
        n.find_error()

    # Справочники-ЗАРПЛАТА-Справочник видов деятельности
    def test_directory_business(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["references"])
        n.click_menu_section(data["menu"]["secondLevel"]["SALARY"])
        n.click_menu_section(data["menu"]["thirdLevel"]["DirectoryBusiness"])
        n.find_error()

    # Справочники-ЗАРПЛАТА-Коэффициент индексации социальных/детских пособий
    def test_coefficient_indexation(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["references"])
        n.click_menu_section(data["menu"]["secondLevel"]["SALARY"])
        n.click_menu_section(data["menu"]["thirdLevel"]["CoefficientIndexation"])
        n.find_error()

    # Справочники-ЗАРПЛАТА-MIN / MAX ограничения б/л по месяцам
    def test_min_max_limit(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["references"])
        n.click_menu_section(data["menu"]["secondLevel"]["SALARY"])
        n.click_menu_alt(data["menu"]["thirdLevel"]["MIN_MAX_limit"])
        n.find_error()

    # Справочники-Справочник регионов
    def test_directory_regions(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["references"])
        n.click_menu_section(data["menu"]["secondLevel"]["DirectoryRegions"])
        n.find_error()

    # Отчеты-Печать форм
    def test_printing_forms(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["reports"])
        n.click_menu_section(data["menu"]["secondLevel"]["PrintingForms"])
        n.find_error()

    # Отчеты-Режим печати
    def test_print_mode(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["reports"])
        n.click_menu_section(data["menu"]["secondLevel"]["PrintMode"])
        n.find_error()

    # Отчеты-Анализ данных
    def test_data_analysis(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["reports"])
        n.click_menu_section(data["menu"]["secondLevel"]["DataAnalysis"])
        n.find_error()

    # Отчеты-Отчёты по сотруднику
    def test_reports_employee(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["reports"])
        n.click_menu_section(data["menu"]["secondLevel"]["ReportsEmployee"])
        n.find_error()