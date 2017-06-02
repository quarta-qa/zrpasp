from pages import *
from setup import *
import os


class TestSuite:

    def test_report_form_SBUV(self):
        #n.file_comparison(data["reportFile"]["PESN15"],8,16)
        compare_files("Протокол расчета страховых взносов с 2015 года.xls")

