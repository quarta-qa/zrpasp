from pages import *
from setup import *
import os


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
        p.select_date("Январь", 2017)
        p.click_by_name("Войти")