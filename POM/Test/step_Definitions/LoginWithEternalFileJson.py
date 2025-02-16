import unittest
from pathlib import Path

from selenium import webdriver
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "../..", ".."))
import json
import time
from POM.Pages.LandingPage import LandingPage
from POM.Pages.LoginPage import LoginPage
from POM.Pages.MyAccountPage import MyAccountPage
from selenium.webdriver.chrome.service import Service

class LoginWithExternalFileJson(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        current_directory = Path(__file__).parent.parent
        driver_path = current_directory.parent.parent / "Drivers" / "chromedriver.exe"
        service = Service(executable_path=str(driver_path))
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_LoginUsingJsonFile(self):
        driver = self.driver
        driver.get("https://automationteststore.com/")
        time.sleep(2)
        lp = LandingPage(driver)
        lp.click_Go_Login()
        logpa = LoginPage(driver)
        time.sleep(2)
        my = MyAccountPage(driver)

        currentLoginJson_directory = Path(__file__).parent.parent
        json_file_path = currentLoginJson_directory.parent.parent / "Datos" / "Login.json"

        #file = open("/Datos/Login.json", "r")
        file = open(json_file_path, "r")
        jsondata = file.read()
        obj = json.loads(jsondata)
        list = obj['users']
        print(list)
        print(len(list))
        for i in range(len(list)):
            username = list[i].get("user")
            password = list[i].get("password")
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

