import time
import unittest
from functools import partial
from pytest_bdd import scenarios, given, when, then
from POM.Pages.CreateUserPage import CreateUserPage
from POM.Pages.LandingPage import LandingPage
from POM.Pages.LoginPage import LoginPage
import HtmlTestRunner


AUTOMATION_PAGE = 'https://automationteststore.com/'


scenarios('../features/CreateUser_Without_Mandatory_Field.feature')

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


@when("I do not fill in any mandatory fields, and I confirm that data")
def step_Not_Fill_Mandatory_Fields_Form(browser):
    cup = CreateUserPage(browser)
    time.sleep(2)
    cup.submit_Button_Continue_whitout_Mandatory_field()
    time.sleep(2)
    x = cup.show_error_Mandatory_Field()
    assert x == '×\nError: You must agree to the Privacy Policy!'
    print("Error al no ingresar campos mandatorios")
    assert cup.show_Mandatory_Field_First_Name() == 'First Name must be between 1 and 32 characters!'
    assert cup.show_Mandatory_Field_Last_Name() == 'Last Name must be between 1 and 32 characters!'
    assert cup.show_Mandatory_Field_Email() == 'Email Address does not appear to be valid!'
    assert cup.show_Mandatory_Field_Address() == 'Address 1 must be between 3 and 128 characters!'
    assert cup.show_Mandatory_Field_City() == 'City must be between 3 and 128 characters!'
    assert cup.show_Mandatory_Field_Region() == 'Please select a region / state!'
    assert cup.show_Mandatory_Field_Zipcode() == 'Zip/postal code must be between 3 and 10 characters!'
    assert cup.show_Mandatory_Field_LoginName() == 'Login name must be alphanumeric only and between 5 and 64 characters!'
    assert cup.show_Mandatory_Field_Password() == 'Password must be between 4 and 20 characters!'


@then("I can't create a new account and I can't login to the page and i can see all the red alerts")
def step_Show_Message():
   print("A new account could not be created, as the mandatory fields are all empty")
   print("All alert messages have been displayed, for empty mandatory fields")



if __name__ == '__main__':
     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\admin\\PycharmProjects\\SegundoProyecto\\Reports'), verbosity=2)


