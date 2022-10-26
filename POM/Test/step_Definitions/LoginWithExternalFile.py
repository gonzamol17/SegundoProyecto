import unittest
from selenium import webdriver
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "../..", ".."))
import xlrd
import time

from POM.Pages.LandingPage import LandingPage
from POM.Pages.LoginPage import LoginPage
from POM.Pages.MyAccountPage import MyAccountPage
import HtmlTestRunner

class LoginWithExternalFile(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("/Drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_LoginUsingXmlFile(self):
        driver = self.driver
        driver.get("https://automationteststore.com/")
        time.sleep(2)
        lp = LandingPage(driver)
        lp.click_Go_Login()
        logpa = LoginPage(driver)
        time.sleep(2)
        my = MyAccountPage(driver)

        #Esta parte toma todas las filas y columnas del archivo excel
        path = "/Datos/Users.xlsx"
        inputWorkbook = xlrd.open_workbook(path)
        inputWorksheet = inputWorkbook.sheet_by_index(0)
        row = inputWorksheet.nrows
        col = inputWorksheet.ncols


        for aux in range(1, inputWorksheet.nrows):
            print(aux)
            username = inputWorksheet.cell_value(aux, 1)
            password = inputWorksheet.cell_value(aux, 2)
            time.sleep(4)
            logpa.do_Login(username, password)
            time.sleep(4)
            my.seleccionar_Logoff()
            time.sleep(2)
            lp.click_Go_Login()
            time.sleep(2)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\admin\\PycharmProjects\\SegundoProyecto\\Reports'), verbosity=2)

