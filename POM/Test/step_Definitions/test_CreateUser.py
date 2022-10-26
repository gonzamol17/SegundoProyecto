import time
import pytest
import driver as driver
from pytest_bdd.parsers import string
from selenium import webdriver
import unittest
from functools import partial
from pytest_bdd import scenarios, given, when, then
from POM.Pages.MyAccountPage import MyAccountPage
from POM.Pages.CreateUserPage import CreateUserPage
from POM.Pages.LandingPage import LandingPage
from POM.Pages.LoginPage import LoginPage
import HtmlTestRunner



AUTOMATION_PAGE = 'https://automationteststore.com/'


scenarios('../features/CreateUser.feature')

@given("I am on the Automation test store page and I select the option to create a new account")
def step_Go_Login_Page_of_Automation_Test_Store(browser):
    browser.get(AUTOMATION_PAGE)
    lp = LandingPage(browser)
    lp.click_Go_Login()
    time.sleep(2)
    lop = LoginPage(browser)
    #check = lop.verify_IsChecked()
    #browser.assertTrue(check, "Está la opción Create Account tildada")
    time.sleep(2)
    lop.submit_Continue()
    time.sleep(2)


@when("I fill in all the fields of the form and I confirm that data")
def step_Fill_All_Fields_Form(browser):
    account = CreateUserPage(browser)
    time.sleep(2)
    account.complete_All_Field_For_New_Account("Lukagesss", "Cornejosssa", "Lukageddd.Cornejosssdd@darwoft.com",
                                               "Sol de Mayo 550", "Cordoba", "5000", "Lukagessdd_Cornejosssss", "River10",
                                               "River10")
    time.sleep(2)
    account.create_Country("Argentina")
    time.sleep(2)
    account.create_Region("Cordoba")
    time.sleep(2)
    account.submit_Button_Continue_whitout_Mandatory_field()


@then("I successfully create my account and verify that I am logged in with my newly created account")
def step_Login_MyAccount_With_New_User(browser):
    myaccount = MyAccountPage(browser)
    time.sleep(2)
    myaccount.continue_Account3()
    time.sleep(2)
    x = myaccount.verificar_Ingreso_Correcto2()
    time.sleep(2)
    #print(x)
    assert x == 'MY ACCOUNT'
    print("Estoy en la página de My account, se ha creado exitosamente la cuenta del nuevo usuario")


if __name__ == '__main__':
     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\admin\\PycharmProjects\\SegundoProyecto\\Reports'), verbosity=2)