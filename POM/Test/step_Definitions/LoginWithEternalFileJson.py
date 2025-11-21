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
        cls.driver.get("https://automationteststore.com/")  # URL abierta aquí

    def test_LoginUsingJsonFile(self):
        driver = self.driver
        lp = LandingPage(driver)
        lp.click_Go_Login()
        login_page = LoginPage(driver)
        my_account = MyAccountPage(driver)

        # Ruta JSON correcta
        root_dir = Path(__file__).resolve().parents[3]
        json_path = root_dir / "Datos" / "Login.json"

        with open(json_path, "r") as file:
            data = json.load(file)

        users = data.get("users", [])
        self.assertTrue(len(users) > 0, "No users found in JSON file")

        for user in users:
            username = user.get("user")
            password = user.get("password")
            login_page.do_Login(username, password)
            time.sleep(3)
            my_account.seleccionar_Logoff()
            time.sleep(1)
            lp.click_Go_Login()
            time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Completed")
