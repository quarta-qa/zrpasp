import pytest

path = "D:\\python\\automation_pytest\\ReportsZrp2.py"
test_suite = "TestSuite"

tests = [
    'test_login',
    'test_payslip'
]

running = []
for i in tests:
    running.append(path + "::" + test_suite + "::" + i)
running.append('--html=report.html')
running.append('--resultlog=D:\\python\\automation_pytest\\log.txt')

pytest.main(running)
