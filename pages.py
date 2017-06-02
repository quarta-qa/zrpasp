from time import sleep
from setup import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from xlutils.copy import copy as xlcopy
from locators import *

import shutil
import json
import os
import glob
import xlrd
import xlwt
import hashlib
import logging
import xlutils
import openpyxl
from datetime import datetime


TIMEOUT = 120

#datetime.date().today()

def load_data(file):
    return json.loads(open('%s.json' % file, encoding="utf8").read())


def get_max_rows_and_cols(file):

    rows_max = 0
    cols_max = 0

    for name in file.sheet_names():
        sheet = file.sheet_by_name(name)
        if rows_max < sheet.nrows:
            rows_max = sheet.nrows
        if cols_max < sheet.ncols:
            cols_max = sheet.ncols

    return [rows_max, cols_max]


# Сравнение excel файлов 1
def analyze_two_files(filename):

    data = load_data("employee")
    file = data["reportFile"]
    reference_file = file["directory"] + filename
    output_file = file["directoryCompare"] + filename

    output_hash = md5(output_file)
    reference_hash = md5(reference_file)
    if output_hash == reference_hash:
        print('Печатные формы одинаковы')
    else:
        # открываем исходный файл
        output = xlrd.open_workbook(output_file, on_demand=True, formatting_info=True)
        reference = xlrd.open_workbook(reference_file, on_demand=True, formatting_info=True)
        if output.nsheets != reference.nsheets:
            print('Количество книг не совпадает')
        else:
            print('Найдены ОШИБКИ в печатной форме: "%s"' % filename)

            output_max = get_max_rows_and_cols(output)
            reference_max = get_max_rows_and_cols(reference)
            max_rows = max(reference_max[0], output_max[0])
            max_cols = max(reference_max[1], output_max[1])

            reference_new = xlcopy(reference)
            for i in range(reference.nsheets):
                sheet = reference_new.get_sheet(i)
                sheet.write(max_rows, max_cols, "!")
            reference_new.save(file["directory"]+"example.xls")

            output_new = xlcopy(output)
            for i in range(output.nsheets):
                sheet = output_new.get_sheet(i)
                sheet.write(max_rows, max_cols, "!")
            output_new.save(file["directory"]+"example_new.xls")

    return [file["directory"]+"example.xls", file["directory"]+"example_new.xls"]


def compare_files(filename):

    files = analyze_two_files(filename)

    reference = xlrd.open_workbook(files[0], on_demand=True,  formatting_info=True)
    output = xlrd.open_workbook(files[1], on_demand=True, formatting_info=True)

    for index in range(reference.nsheets):
        reference_sheet = reference.sheet_by_index(index)
        output_sheet = output.sheet_by_index(index)
        reference_sheet_name = reference_sheet.name
        output_sheet_name = output_sheet.name
        if reference_sheet_name != output_sheet_name:
            print("Название книги[%s] не совпадает с эталонным [%s]!"% (output_sheet_name,reference_sheet_name))
        print("Книга [%s]:" % reference_sheet_name)
        for i in range(reference_sheet.nrows):
            for j in range(reference_sheet.ncols):
                reference_cell = reference_sheet.cell(i, j).value
                output_cell = output_sheet.cell(i, j).value
                if reference_cell != output_cell:
                    print("\tЯчейка [%s, %s]. Значение [%s] не совпадает с эталонным [%s]!"
                          % (i, j, output_cell, reference_cell))


# Получение хеша
def md5(filename):
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
#
def delete_spaces(value):
    return value.strip()

class BasePage(object):


    def __init__(self, driver):
        self.driver = driver



    # Массовый чекбокс
    def select_employee(self, value):
        element = self.driver.find_element(By.XPATH, "//tr[contains(., '%s')]" % value)
        element.find_element(By.XPATH, ".//input[@type='checkbox']").click()

    # присвоить значение полю
    def set_value(self, locator, value):
        if value:
            element = self.wait(locator)
            element.click()
            element.clear()
            element.send_keys(value)

    # заглушка для очистки
    def clear_date_field(self, locator):
        element = self.wait(locator)
        element.click
        element.send_keys('\b\b\b\b\b\b\b\b' + Keys.ENTER)

    # заполнение даты
    def set_date(self, locator, value):
        if value:
            element = self.wait(locator)
            element.clear()
            element.send_keys(value + Keys.RETURN)
            WebDriverWait(self.driver, TIMEOUT).until(EC.invisibility_of_element_located((By.ID, "ui-datepicker-div")))

    # заполнение выпадающего списка
    def set_dropdown(self, locator, value):
        if value:
            element = self.wait(locator)
            element.click()
            self.click((By.XPATH, "//li[text()='%s']" % value))

    # чекбокс
    def set_checkbox(self, locator, value):
        element = self.wait(locator)
        if element.is_selected() != value:
            element.click()
            self.wait_for_loading()

    # поиск все поля
    def search(self, value):
        elements = self.driver.find_elements_by_xpath("//input[@placeholder='Все поля']")
        for i in elements:
            i.send_keys(value + Keys.RETURN)

    # заполнение из вложенного справочника
    def set_type(self, locator, value, label=""):
        if value:
            element = self.wait(locator).find_element(By.XPATH, ".//following-sibling::*[1]/button[2]")
            element.click()
            sleep(5)
            self.search(value)
            self.click((By.XPATH, "//span[normalize-space(text())='Выбрать']"))

    # заполнение из вложенного справочника альтернатива
    def set_type_alt(self, value):
        if value:
            self.search(value)
            self.click_by_name("Выбрать")

    # заполнение выподающего списка select
    def set_select(self, value, label=""):
        if value:
            element = WebDriverWait(self.driver, TIMEOUT).until(
                EC.visibility_of_element_located((By.XPATH, "//select[contains(., '%s')]" % value)))
            Select(element).select_by_visible_text(value)

    #
    def delete_spaces(self, value):
        return value.strip()

    # клик
    def click(self, locator):
        element = self.wait(locator)
        webdriver.ActionChains(self.driver).move_to_element(element).perform()
        element.click()
        self.wait_for_loading()

    # выбор меню
    def click_menu(self, locator):
        sleep(1)
        element = self.wait(locator)
        webdriver.ActionChains(self.driver).move_to_element(element).perform()
        element.click()
        self.wait_for_loading()

    # выбор скрытого меню
    def click_menu_alt(self, value):
        sleep(1)
        element = self.driver.find_element(By.XPATH, "//span[.='%s']" % value)
        webdriver.ActionChains(self.driver).move_to_element(element).perform()
        element.click()
        self.wait_for_loading()

    # клик по имени
    def click_by_name(self, value, exactly=False, order=1):
        if exactly:
            element = self.wait((By.XPATH, "(//*[self::button or self::a][.='%s'])[%s]" % (value, order)))
        else:
            element = self.wait((By.XPATH, "(//*[self::button or self::a][contains(normalize-space(), '%s')])[%s]" % (value, order)))
        webdriver.ActionChains(self.driver).move_to_element(element).perform()
        element.click()
        self.wait_for_loading()

    # выбор из грида
    def click_on_employee(self, value):
        element = self.wait((By.XPATH, "//*[self::a or self::span][.='%s']" % value))
        webdriver.ActionChains(self.driver).move_to_element(element).perform()
        element.click()
        self.wait_for_loading()

    # ожидание
    def wait(self, locator):
        return WebDriverWait(self.driver, TIMEOUT).until(
            EC.visibility_of_element_located(locator))

    # ожидание загрузки
    def wait_for_loading(self):
        WebDriverWait(self.driver, TIMEOUT).until(EC.invisibility_of_element_located((By.ID, "loadingSpinner")))
        WebDriverWait(self.driver, TIMEOUT).until(
            EC.invisibility_of_element_located((By.XPATH, "//div[text()='Данные загружаются']")))

    # ПРОВЕРКА НА ОШИБКИ
    def find_error(self):
        # if self.driver.find_element_by_xpath("//span[.='ajax (XHR) POST request warn (details are in the console)']"):
        #     return False
        # return True
        try:
            self.driver.find_element_by_xpath("//span[.='ajax (XHR) POST request warn (details are in the console)']")
            print('fail')
        except:
            print('success')
        self.driver.get(Links.main_page)

    # ПРОВЕРКА наличия файла в директории
    def file_inspect(self, namefile):
        sleep(10)
        data = load_data("employee")
        os.chdir(data["reportFile"]["directory"])
        if glob.glob(namefile):
            print('Отчет:' + namefile)
        else:
            print('No report file')
            self.driver.save_screenshot(namefile+'.png')
            self.driver.get(Links.main_page)
            os.chdir(data["reportFile"]["directoryDefault"])
            assert glob.glob(namefile)
        os.chdir(data["reportFile"]["directoryDefault"])
        print("Link: %s" % data["reportFile"]["directory"]+namefile)

    # Сравнение excel файлов

    def file_comparison (self, namefile,zrov,zcol):
        data = load_data("employee")

        rlhesh =self.md5(data["reportFile"]["directory"]+namefile)
        elhesh =self.md5(data["reportFile"]["directoryCompare"]+namefile)
        if rlhesh == elhesh:
            print('Печатные формы одинаковы')

        else:
            # открываем исходный файл
            rl = xlrd.open_workbook(filename=data["reportFile"]["directory"] + namefile)
            el = xlrd.open_workbook(filename=data["reportFile"]["directoryCompare"] + namefile)
            booksr = len(rl.sheets())
            # print(booksr)
            bookse = len(el.sheets())
            # print(bookse)
            if booksr != bookse:
                print('Количество книг не совпадает')

            else:
                print('Найдены ОШИБКИ в печатной форме: "' +namefile+'"')
                i = 0
                while i < bookse:
                    sheetr = rl.sheet_by_index(i)
                    valsrl = [sheetr.row_values(rownum) for rownum in range(sheetr.nrows)]

                    #print(valsrl)
                    sheete = el.sheet_by_index(i)
                    valsel = [sheete.row_values(rownum) for rownum in range(sheete.nrows)]
                    sheete_name = el.sheet_names()
                    #print(valsel)
                    if valsrl != valsel:

                        print('На листе:"'+sheete_name[i]+'"')

                        for xl in range(zrov):
                            for yl in range(zcol):
                                valr = sheetr.row_values(xl)[yl]
                                vale = sheete.row_values(xl)[yl]
                                if valr!= vale:
                                    print(
                                        'В ячейке ',xl+1,':',yl+1,' Значение="',valr,'" не совпадает с эталонным ="',
                                        vale,'"')

                                #print(xl,yl)

                    else:
                        print('На листе:"'+sheete_name[i]+' Ошибок нет')

                    i =i+ 1



        # чекбокс по имени
    def select_check_by_name(self, value, stat):
        element = self.driver.find_element(By.XPATH, "//label[contains(text(),'%s')]" % value)
        cb = element.find_element(By.XPATH, ".//following-sibling::input[@type='checkbox']")
        cb.click()
        if cb.is_selected() != stat:
            cb.click()
            self.wait_for_loading()

        # чекбокс по имени2
    def select_check_name_alt(self, value, stat):
        element = self.driver.find_element(By.XPATH, "//div[@metadata='metadata[key]' and contains(., '%s')]" % value)
        cb = element.find_element(By.XPATH, ".//input[@type='checkbox']")

        if cb.is_selected() != stat:
            cb.click()
            self.wait_for_loading()

    # заполнение поля по имени
    def select_val_by_name(self, value, inf):
        element = self.driver.find_element(By.XPATH, "//label[contains(text(),'%s')]" % value)
        field = element.find_element(By.XPATH, ".//following-sibling::input[@type='text']")
        field.clear()
        field.send_keys(inf)
        self.wait_for_loading()

    # Выбор фамилии из списка

    def click_list_my(self, value):
        self.search(value)
        sleep(2)
        self.select_employee(value)
        sleep(2)
        element = self.driver.find_element(By.XPATH, "//div[@title='Очистить поиск']")
        element.click()


class LoginPage(BasePage):

    def username(self, value):
        self.set_value(LoginLocators.username, value)

    def password(self, value):
        self.set_value(LoginLocators.password, value)

        #
    def select_date(self, month, year):
        self.click((By.XPATH, "(//input[@type='text'])[2]"))
        current_year = int(self.wait((By.XPATH, "//li[@class='presently']")).text)
        if year > current_year+2 or year < current_year-2:
            if year < current_year-2:
                upper = current_year-2
                flag = False
                while not flag:
                    self.click((By.XPATH, "//span[@class='qa-icon-next']"))
                    sleep(1)
                    if (year < upper) and (year >= upper-5):
                        flag = True
                    else:
                        upper -= 5
            elif year > current_year+2:
                lower = current_year+2
                flag = False
                while not flag:
                    self.click((By.XPATH, "//span[@class='qa-icon-prev']"))
                    sleep(1)
                    if (year > lower) and (year <= lower+5):
                        flag = True
                    else:
                        lower += 5
        self.click((By.XPATH, "//li[@class='past' or @class='future' or @class='presently'][.='%s']" % year))
        self.click((By.XPATH, "//div[@class='cell-highlight'][.='%s']" % month))

    def lot(self):
        self.click(LoginLocators.lot)
        self.click(LoginLocators.lotznachnumber)




class MenuPage(BasePage):

    def click_button_menu(self):
        self.driver.get(Links.main_page)
        sleep(5)
        self.click(MenuLocators.menu)


    def click_menu_section(self, value):
        self.click_menu((By.XPATH, "//span[.='%s']" % value))
        print(value)

    def click_menu_section_alt(self, value):
        self.click_menu_alt(value)


