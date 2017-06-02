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

    # Справочники-Сотрудники
    def test_eployees(self):
        data = load_data("menu")

        n = MenuPage(self.driver)
        n.wait_for_loading()
        n.click_button_menu()
        n.click_menu_section(data["menu"]["firstLevel"]["references"])
        n.click_menu_section(data["menu"]["secondLevel"]["Employees"])
        n.find_error()

    def test_eployees_displacement(self):
        data = load_data("employee")
        n = BasePage(self.driver)
        n.wait_for_loading()
        n.search(data["employeedata"]["name"])
        n.click_by_name("Открыть")
        n.click_by_name("Перемещение ЛС")
        n.click_by_name("Да")







