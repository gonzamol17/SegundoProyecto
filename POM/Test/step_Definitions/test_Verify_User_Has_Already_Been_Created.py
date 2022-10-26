import time
import unittest
from pytest_bdd import scenarios, given, when, then
from POM.Pages.CreateUserPage import CreateUserPage
from POM.Pages.LandingPage import LandingPage
from POM.Pages.LoginPage import LoginPage

import HtmlTestRunner



AUTOMATION_PAGE = 'https://automationteststore.com/'


scenarios('../features/Verify_User_Has_Already_Been_Created.feature')

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


@when("I fill in all the fields of the form, with data from an existing user and I confirm that data")
def step_Complete_Data_With_Already_exist(browser):
    account = CreateUserPage(browser)
    time.sleep(2)
    account.complete_All_Field_For_New_Account("Gonzalo", "Molina", "gonzalo.molina@darwoft.com",
                                               "Sol de Mayo 550", "Cordoba", "5000", "gonza_mol", "Chicharito10",
                                               "Chicharito10")

    time.sleep(2)
    account.create_Country("Argentina")
    time.sleep(2)
    account.create_Region("Cordoba")
    time.sleep(2)
    account.submit_Button_Continue_whitout_Mandatory_field()
    time.sleep(2)
    x = account.show_Existing_User_Message()
    print(x)
    assert x == '×\nError: E-Mail Address is already registered!'
    print("Error al querer crear una cuenta de un usuario ya existente")


@then("The system does not have to create that existing user again, and it has to inform me that already exists")
def step_Message():
    print("The user could not be created, because it already exists in the system")




if __name__ == '__main__':
     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\admin\\PycharmProjects\\SegundoProyecto\\Reports'), verbosity=2)