from pages import *
from setup import *
import os


class TestSuite:

    # def setup_method(self):
    #     """


    #     Тут описывается что происходит ПЕРЕД запуском всех тестов.
    #     Сейчас тут описан драйвер, а также подготовка окна браузера и
    #     переход на нужную ссылку.
    #     """
    #     self.driver = webdriver.Chrome("C:\Python34\Scripts\chromedriver.exe")
    #     self.driver.maximize_window()
    #     self.driver.get(Links.main_page)
    #
    #     data = load_data("logpas")
    #
    #     p = LoginPage(self.driver)
    #     p.username(data["username"])
    #     p.password(data["password"])
    #     p.lot()
    #     p.select_date("Январь", 2017)
    #     p.click_by_name("Войти")
    #
    # def teardown_method(self):
    #     """
    #     Тут описывается что происходит ПОСЛЕ запуском всех тестов.
    #     Сейчас тут просто убивается драйвер после прогона.
    #     """
    #     self.driver.quit()

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
        p.select_date("Январь", 2017)
        p.click_by_name("Войти")

        # Структура подразделений
    def test_employees_reports(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["structure"])
        data = load_data("employee")
        n = BasePage(self.driver)
        n.wait_for_loading()
        n.search(data["employeeData"]["name"])
        n.click_by_name("Карточка расчета ЗП")
        n.click_by_name("Отчеты по сотруднику")
        n.click_by_name("Расч. листок/итоги", True)
        n.click_by_name("Сохранить", False, 2)

        self.driver.get(Links.main_page)

    def test_new_payslip(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["structure"])
        data = load_data("employee")
        n = BasePage(self.driver)
        n.wait_for_loading()
        n.search(data["employeeData"]["name"])
        n.click_by_name("Карточка расчета ЗП")
        n.click_by_name("Отчеты по сотруднику")
        sleep(1)
        n.click_by_name("Расч. листок", True)
        n.click_by_name("Нет")
        n.file_inspect(data["reportFile"]["newPayslip"])
        self.driver.get(Links.main_page)

    def test_new_estimated_ved(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["structure"])
        data = load_data("employee")
        n = BasePage(self.driver)
        n.search(data["employeeData"]["name"])
        n.click_by_name("Карточка расчета ЗП")
        n.click_by_name("Отчеты по сотруднику")
        n.click_by_name("Расч. ведомость", True)
        n.click_by_name("Сохранить", False, 2)
        n.file_inspect(data["reportFile"]["estimatedVedomost"])
        self.driver.get(Links.main_page)

    def test_1ndfl(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["structure"])
        data = load_data("employee")
        n = BasePage(self.driver)
        n.wait_for_loading()
        n.search(data["employeeData"]["name"])
        n.click_by_name("Карточка расчета ЗП")
        n.click_by_name("Отчеты по сотруднику")
        n.click_by_name("Налог. регистр (1-НДФЛ)", True)
        sleep(5)
        n.file_inspect(data["reportFile"]["1ndfl"])
        self.driver.get(Links.main_page)

    def test_litsIndividKart(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["structure"])
        data = load_data("employee")
        n = BasePage(self.driver)
        n.search(data["employeeData"]["name"])
        n.click_by_name("Карточка расчета ЗП")
        data = load_data("employee")
        n = BasePage(self.driver)
        n.wait_for_loading()
        n.click_by_name("Отчеты по сотруднику")
        n.click_by_name("Лиц.сч. (индивид.карт.) по  страх.взносам", True)
        n.file_inspect(data["reportFile"]["LitsSchIndividKart"])
        self.driver.get(Links.main_page)

    def test_faceCard(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["structure"])
        data = load_data("employee")
        n = BasePage(self.driver)
        n.search(data["employeeData"]["name"])
        n.click_by_name("Карточка расчета ЗП")
        data = load_data("employee")
        n = BasePage(self.driver)
        n.click_by_name("Отчеты по сотруднику")
        n.click_by_name("Лицевая карточка", True)
        n.click_by_name("Сохранить", False, 2)
        n.file_inspect(data["reportFile"]["LitsSchIndividKart"])
        self.driver.get(Links.main_page)

    def test_formT_54a(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["structure"])
        data = load_data("employee")
        n = BasePage(self.driver)
        n.search(data["employeeData"]["name"])
        n.click_by_name("Карточка расчета ЗП")
        n.click_by_name("Отчеты по сотруднику")
        n.click_by_name("Лицевой счет (форма Т-54а)", True)
        n.file_inspect(data["reportFile"]["formT_54a"])
        self.driver.get(Links.main_page)

    def test_dividends_statements(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["structure"])
        data = load_data("employee")
        n = BasePage(self.driver)
        n.wait_for_loading()
        n.search(data["employeeData"]["name"])
        n.click_by_name("Карточка расчета ЗП")
        n.click_by_name("Отчеты по сотруднику")
        n.click_by_name("Выплаты по ведомостям", True)
        n.click_by_name("Сохранить", False, 2)
        n.file_inspect(data["reportFile"]["dividendsStatements"])
        self.driver.get(Links.main_page)

    def test_swim_per_month(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["structure"])
        data = load_data("employee")
        n = BasePage(self.driver)
        n.wait_for_loading()
        n.search(data["employeeData"]["name"])
        n.click_by_name("Карточка расчета ЗП")
        n.click_by_name("Отчеты по сотруднику")
        n.click_by_name("Выпл. сотр. за месяц", True)
        n.set_select("Сбербанк")
        n.click_by_name("Сохранить", False, 2)
        n.file_inspect(data["reportFile"]["swimPerMonth"])
        self.driver.get(Links.main_page)

    def test_typical_personal_account(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["structure"])
        data = load_data("employee")
        n = BasePage(self.driver)
        n.wait_for_loading()
        n.search(data["employeeData"]["name"])
        n.click_by_name("Карточка расчета ЗП")
        n.click_by_name("Отчеты по сотруднику")
        n.click_by_name("Типовой лицевой счет", True)
        n.file_inspect(data["reportFile"]["typicalPersonalAccount"])
        self.driver.get(Links.main_page)

    def test_data_insurance_premiums(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["structure"])
        data = load_data("employee")
        n = BasePage(self.driver)
        n.wait_for_loading()
        n.search(data["employeeData"]["name"])
        n.click_by_name("Карточка расчета ЗП")
        n.click_by_name("Отчеты по сотруднику")
        n.click_by_name("Сведения о страховых взносах", True)
        n.file_inspect(data["reportFile"]["dataInsurancePremiums"])
        self.driver.get(Links.main_page)

    def test_information_gni(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["structure"])
        data = load_data("employee")
        n = BasePage(self.driver)
        n.wait_for_loading()
        n.search(data["employeeData"]["name"])
        n.click_by_name("Карточка расчета ЗП")
        n.click_by_name("Отчеты по сотруднику")
        n.click_by_name("Справки", True)
        n.click_by_name("Справ. в ГНИ (2-НДФЛ)", True)
        n.file_inspect(data["reportFile"]["informationGNI"])
        self.driver.get(Links.main_page)

    def test_information_gossluzh_about_earnings(self):

        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["structure"])
        data = load_data("employee")
        n = BasePage(self.driver)
        n.wait_for_loading()
        n.search(data["employeeData"]["name"])
        n.click_by_name("Карточка расчета ЗП")
        n.click_by_name("Отчеты по сотруднику")
        n.click_by_name("Справки", True)
        n.click_by_name("Справ. о заработке госслуж.", True)
        n.set_date(ReportsEmployeeLocators.beginningOfPeriod, "01.01.2016")
        n.click(ReportsEmployeeLocators.endOfThePeriod)
        n.wait_for_loading()
        n.set_date(ReportsEmployeeLocators.endOfThePeriod, "31.12.2016")
        n.wait_for_loading()
        sleep(5)
        n.click_by_name("Сохранить", False, 2)
        n.wait_for_loading()
        sleep(1)
        n.click_by_name("Сохранить", False, 2)
        n.wait_for_loading()
        sleep(5)
        n.click_by_name("Сохранить", False, 2)
        n.wait_for_loading()
        sleep(5)
        n.file_inspect(data["reportFile"]["informationGosSluzhAboutEarnings"])
        self.driver.get(Links.main_page)

    def te1st_information_salary_for_the_period(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["structure"])
        data = load_data("employee")
        n = BasePage(self.driver)
        n.wait_for_loading()
        n.search(data["employeeData"]["name"])
        n.click_by_name("Карточка расчета ЗП")
        n.click_by_name("Отчеты по сотруднику")
        n.click_by_name("Справки", True)
        n.click_by_name("Справ. о з/п за период", True)
        n.set_date(ReportsEmployeeLocators.beginSalary, "0116")
        n.wait_for_loading()
        n.set_date(ReportsEmployeeLocators.endSalary, "1216")
        n.wait_for_loading()
        n.set_checkbox(ReportsEmployeeLocators.considerСulations, True)
        n.wait_for_loading()
        n.set_checkbox(ReportsEmployeeLocators.accordingАrchives, True)
        n.wait_for_loading()
        n.click_by_name("Сохранить", False, 2)
        n.file_inspect(data["reportFile"]["informationSalaryForThePeriod"])
        self.driver.get(Links.main_page)

    def test_information_pensionable(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["structure"])
        data = load_data("employee")
        n = BasePage(self.driver)
        n.wait_for_loading()
        n.search(data["employeeData"]["name"])
        n.click_by_name("Карточка расчета ЗП")
        n.click_by_name("Отчеты по сотруднику")
        n.click_by_name("Справки", True)
        n.click_by_name("Справ. для пенсии", True)
        n.set_date(ReportsEmployeeLocators.beginPFR, "0116")
        n.wait_for_loading()
        n.set_date(ReportsEmployeeLocators.endPFR, "1216")
        n.wait_for_loading()
        n.set_checkbox(ReportsEmployeeLocators.archivesPFR, True)
        n.wait_for_loading()
        n.set_checkbox(ReportsEmployeeLocators.considerPFR, True)
        n.wait_for_loading()
        n.click_by_name("Сохранить", False, 2)
        n.file_inspect(data["reportFile"]["informationPensionable"])
        self.driver.get(Links.main_page)

    def test_information_for_loans(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["structure"])
        data = load_data("employee")
        n = BasePage(self.driver)
        n.wait_for_loading()
        n.search(data["employeeData"]["name"])
        n.click_by_name("Карточка расчета ЗП")
        n.click_by_name("Отчеты по сотруднику")
        n.click_by_name("Справки", True)
        n.click_by_name("Справ. для ссуды", True)
        n.click_by_name("Да", True)
        sleep(3)
        n.set_date(ReportsEmployeeLocators.beginForLoans, "0116")
        n.wait_for_loading()
        n.set_date(ReportsEmployeeLocators.endForLoans, "1216")
        n.wait_for_loading()
        n.set_value(ReportsEmployeeLocators.branchBank, "Отделение СБ РФ- 158 Отделение Сбербанка Москвы")
        n.wait_for_loading()
        n.click_by_name("Сохранить", False, 2)
        n.wait_for_loading()
        sleep(13)
        n.click_by_name("Сохранить", False, 2)
        n.file_inspect(data["reportFile"]["informationForLoans"])
        self.driver.get(Links.main_page)

    def test_information_for_exchange(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["structure"])
        data = load_data("employee")
        n = BasePage(self.driver)
        n.wait_for_loading()
        n.search(data["employeeData"]["name"])
        n.click_by_name("Карточка расчета ЗП")
        n.click_by_name("Отчеты по сотруднику")
        n.click_by_name("Справки", True)
        n.click_by_name("Справ. для биржи", True)
        n.set_date(ReportsEmployeeLocators.dateOfIssue, "16.02.2017")
        n.wait_for_loading()
        n.set_date(ReportsEmployeeLocators.monthIndexing, "1003")
        n.wait_for_loading()
        n.set_value(ReportsEmployeeLocators.informationMonths, "12")
        n.wait_for_loading()
        n.set_value(ReportsEmployeeLocators.averageEarningsMonths, "12")
        n.wait_for_loading()
        n.set_checkbox(ReportsEmployeeLocators.considerRecalculations, True)
        n.wait_for_loading()
        n.set_checkbox(ReportsEmployeeLocators.archives, True)
        n.wait_for_loading()
        n.click_by_name("Сохранить", False, 2)
        # n.wait_for_loading()
        # n.click_by_name("Сохранить", False, 2)
        n.file_inspect(data["reportFile"]["informationForExchange"])
        self.driver.get(Links.main_page)

    def test_information_for_prikomand(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["structure"])
        data = load_data("employee")
        n = BasePage(self.driver)
        n.wait_for_loading()
        n.search(data["employeeData"]["name"])
        n.click_by_name("Карточка расчета ЗП")
        n.click_by_name("Отчеты по сотруднику")
        n.click_by_name("Справки", True)
        n.click_by_name("Справ. для прикоманд.", True)
        n.set_date(ReportsEmployeeLocators.beginForPrikomand, "0116")
        n.wait_for_loading()
        n.set_date(ReportsEmployeeLocators.endForPrikomand, "1216")
        n.wait_for_loading()
        n.click_by_name("Сохранить", False, 2)
        n.wait_for_loading()
        n.click_by_name("Сохранить", False, 2)
        n.file_inspect(data["reportFile"]["informationForPrikomand"])
        self.driver.get(Links.main_page)

    def test_information_for_the_consulate(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["structure"])
        data = load_data("employee")
        n = BasePage(self.driver)
        n.wait_for_loading()
        n.search(data["employeeData"]["name"])
        n.click_by_name("Карточка расчета ЗП")
        n.click_by_name("Отчеты по сотруднику")
        n.click_by_name("Справки", True)
        n.click_by_name("Справ. для консульства", True)
        n.set_date(ReportsEmployeeLocators.beginTheConsulate, "0116")
        n.wait_for_loading()
        n.set_date(ReportsEmployeeLocators.endTheConsulate, "1216")
        n.wait_for_loading()
        n.set_value(ReportsEmployeeLocators.forSubmissionTo, "Посольство Китая")
        n.wait_for_loading()
        n.set_checkbox(ReportsEmployeeLocators.theConsulateEarningsMonths, True)
        n.wait_for_loading()
        n.click_by_name("Сохранить", False, 2)
        n.file_inspect(data["reportFile"]["informationForTheConsulate"])
        self.driver.get(Links.main_page)

    def test_information_prikomand_3(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["structure"])
        data = load_data("employee")
        n = BasePage(self.driver)
        n.wait_for_loading()
        n.search(data["employeeData"]["name"])
        n.click_by_name("Карточка расчета ЗП")
        n.click_by_name("Отчеты по сотруднику")
        n.click_by_name("Справки", True)
        n.click_by_name("Справ. для прикоманд.(3 мес.)", True)
        n.set_date(ReportsEmployeeLocators.beginForPrikomand3, "0117")
        n.wait_for_loading()
        n.set_date(ReportsEmployeeLocators.dateInformation, "1216")
        n.wait_for_loading()
        n.click_by_name("Сохранить", False, 2)
        n.file_inspect(data["reportFile"]["informationForPrikomand_3"])
        self.driver.get(Links.main_page)

    def test_information_salary_12_months(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["structure"])
        data = load_data("employee")
        n = BasePage(self.driver)
        n.wait_for_loading()
        n.search(data["employeeData"]["nameOfTheDismissed"])
        n.click_by_name("Карточка расчета ЗП")
        n.click_by_name("Отчеты по сотруднику")
        n.click_by_name("Справки", True)
        n.click_by_name("Справ.о з/п за 12 м.и выпл.при увол.", True)
        n.set_checkbox(ReportsEmployeeLocators.archivesSalary12months, True)
        n.wait_for_loading()
        n.click_by_name("Сохранить", False, 2)
        n.wait_for_loading()
        n.file_inspect(data["reportFile"]["informationsalary12monthsPaymentSeverance"])
        self.driver.get(Links.main_page)

    def test_note_calculation_of_severance(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["structure"])
        data = load_data("employee")
        n = BasePage(self.driver)
        n.wait_for_loading()
        n.search(data["employeeData"]["nameOfTheDismissed"])
        n.click_by_name("Карточка расчета ЗП")
        n.click_by_name("Отчеты по сотруднику")
        n.click_by_name("Справки", True)
        n.click_by_name("Записка-расчет при увольнении(T-61)", True)
        n.wait_for_loading()
        n.file_inspect(data["reportFile"]["noteCalculationOfSeverance"])
        self.driver.get(Links.main_page)

    def test_calc_protocol(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["structure"])
        data = load_data("employee")
        n = BasePage(self.driver)
        n.wait_for_loading()
        n.search(data["employeeData"]["nameHolidayToCareForTheChild"])
        n.click_by_name("Карточка расчета ЗП")
        n.search("102")
        n.wait_for_loading()
        n.click_by_name("Отчеты по сотруднику")
        n.click_by_name("Справки", True)
        n.click_by_name("Протокол расч. ср. зар.  до 1.5 лет", True)
        n.wait_for_loading()
        n.file_inspect(data["reportFile"]["calcProtocol"])
        self.driver.get(Links.main_page)

    def te1st_information_knd_1151087(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["structure"])
        data = load_data("employee")
        n = BasePage(self.driver)
        n.wait_for_loading()
        n.search(data["employeeData"]["information_knd_1151087"])
        n.click_by_name("Карточка расчета ЗП")
        n.click_by_name("Отчеты по сотруднику")
        n.click_by_name("Справки", True)
        n.click_by_name("Справка в ФНС по ДСВ (КНД 1151087)", True)
        n.wait_for_loading()
        n.file_inspect(data["reportFile"]["information_knd_1151087"])
        self.driver.get(Links.main_page)

    def test_informationon_earnings_RUSZN(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["structure"])
        data = load_data("employee")
        n = BasePage(self.driver)
        n.wait_for_loading()
        n.search(data["employeeData"]["name"])
        n.click_by_name("Карточка расчета ЗП")
        n.click_by_name("Отчеты по сотруднику")
        n.click_by_name("Справки", True)
        n.click_by_name("Справка о заработке для РУСЗН", True)
        n.wait_for_loading()
        n.set_checkbox(ReportsEmployeeLocators.archivesRUSZN, True)
        n.wait_for_loading()
        n.set_checkbox(ReportsEmployeeLocators.RecalculationsRUSZN, True)
        n.wait_for_loading()
        n.click_by_name("Сохранить", False, 2)
        n.wait_for_loading()
        n.file_inspect(data["reportFile"]["informationonEarningsForRUSZN"])
        self.driver.get(Links.main_page)

    def test_protocol_calculating_for_children_disabilities(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["structure"])
        data = load_data("employee")
        n = BasePage(self.driver)
        n.wait_for_loading()
        n.search(data["employeeData"]["nameForChildrenDisabilities"])
        n.click_by_name("Карточка расчета ЗП")
        n.click_by_name("Добавить")
        n.click_by_name("Начисление")
        n.wait_for_loading()
        n.search("82")
        n.click_by_name("Выбрать", False, 3)
        n.wait_for_loading()
        n.set_date(ReportsEmployeeLocators.beginChildrenDisabilities, "01.02.2017")
        n.wait_for_loading()
        n.set_date(ReportsEmployeeLocators.endChildrenDisabilities, "05.02.2017")
        n.wait_for_loading()
        sleep(5)
        n.set_date(ReportsEmployeeLocators.dateChildrenDisabilities, "01.02.2017")
        n.wait_for_loading()
        n.set_value(ReportsEmployeeLocators.orderNumberChildrenDisabilities, "145")
        n.wait_for_loading()
        n.click_by_name("Сохранить", False, 2)
        n.wait_for_loading()
        n.click_by_name("Да", True)
        n.wait_for_loading()
        sleep(5)
        n.click_by_name("Расчеты", False, 2)
        sleep(2)
        n.click_by_name("Выпл. (расчет+восст.НДФЛ)")
        n.wait_for_loading()
        sleep(5)
        n.click_by_name("Отчеты по сотруднику")
        sleep(5)
        n.click_by_name("Справки", True)
        n.click_by_name("Протокол расчета среднего заработка для детей-инвалидов", True)
        n.wait_for_loading()
        n.file_inspect(data["reportFile"]["TheProtocolCalculatingAverageEarningsForChildrenDisabilities"])
        n.click_by_name("Удалить", False, 2)
        n.wait_for_loading()
        sleep(5)
        n.click_by_name("Да", True)
        sleep(5)
        self.driver.get(Links.main_page)

    def test_protocol_calculating_hospital(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["structure"])
        data = load_data("employee")
        n = BasePage(self.driver)
        n.wait_for_loading()
        n.search(data["employeeData"]["name"])
        n.click_by_name("Карточка расчета ЗП")
        n.click_by_name("Журнал больничных листов")
        n.click_by_name("Печать", False, 2)
        n.wait_for_loading()
        n.file_inspect(data["reportFile"]["protocolСalculatingHospital"])
        self.driver.get(Links.main_page)

    def test_protcalc_hospital_no_gos(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["structure"])
        data = load_data("employee")
        n = BasePage(self.driver)
        n.wait_for_loading()
        n.search(data["employeeData"]["nameNoGos"])
        n.click_by_name("Карточка расчета ЗП")
        n.click_by_name("Журнал отпусков",False, 2)
        n.search("34")
        n.click_by_name("Печать", False, 2)
        n.click_by_name("Протокол расчета ср.заработка")
        n.wait_for_loading()
        n.file_inspect(data["reportFile"]["protСalcHospitalNoGos"])
        self.driver.get(Links.main_page)

    def test_protcalc_hospital_gos(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["structure"])
        data = load_data("employee")
        n = BasePage(self.driver)
        n.wait_for_loading()
        n.search(data["employeeData"]["name"])
        n.click_by_name("Карточка расчета ЗП")
        n.click_by_name("Журнал отпусков",False, 2)
        n.search("34")
        n.click_by_name("Печать", False, 2)
        n.click_by_name("Протокол расчета ср.заработка")
        n.wait_for_loading()
        n.file_inspect(data["reportFile"]["protСalcHospitalGos"])
        self.driver.get(Links.main_page)

    def test_calculation_05044425_no_gos(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["structure"])
        data = load_data("employee")
        n = BasePage(self.driver)
        n.wait_for_loading()
        n.search(data["employeeData"]["nameNoGos"])
        n.click_by_name("Карточка расчета ЗП")
        n.click_by_name("Журнал отпусков",False, 2)
        n.click_by_name("Печать", False, 2)
        n.click_by_name("Записка-расчет (ф.05044425 по 25Н)")
        n.wait_for_loading()
        n.file_inspect(data["reportFile"]["calculation_05044425_NoGos"])
        self.driver.get(Links.main_page)

    def test_calculation_05044425(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["structure"])
        data = load_data("employee")
        n = BasePage(self.driver)
        n.wait_for_loading()
        n.search(data["employeeData"]["name"])
        n.click_by_name("Карточка расчета ЗП")
        n.click_by_name("Журнал отпусков",False, 2)
        n.click_by_name("Печать", False, 2)
        n.click_by_name("Записка-расчет (ф.05044425 по 25Н)")
        n.wait_for_loading()
        n.file_inspect(data["reportFile"]["calculation_05044425"])
        self.driver.get(Links.main_page)

    def test_unified_form_t60_no_gos(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["structure"])
        data = load_data("employee")
        n = BasePage(self.driver)
        n.wait_for_loading()
        n.search(data["employeeData"]["nameNoGos"])
        n.click_by_name("Карточка расчета ЗП")
        n.click_by_name("Журнал отпусков", False, 2)
        n.click_by_name("Печать", False, 2)
        n.click_by_name("Унифицированная форма № Т-60")
        n.wait_for_loading()
        n.file_inspect(data["reportFile"]["unified_form_T60_NoGos"])
        self.driver.get(Links.main_page)

    def test_unified_form_t60_gos(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["documentation"])
        n.click_menu_section(data["menu"]["secondLevel"]["structure"])
        data = load_data("employee")
        n = BasePage(self.driver)
        n.wait_for_loading()
        n.search(data["employeeData"]["name"])
        n.click_by_name("Карточка расчета ЗП")
        n.click_by_name("Журнал отпусков", False, 2)
        n.click_by_name("Печать", False, 2)
        n.click_by_name("Унифицированная форма № Т-60")
        n.wait_for_loading()
        n.file_inspect(data["reportFile"]["unified_form_T60"])
        self.driver.get(Links.main_page)



