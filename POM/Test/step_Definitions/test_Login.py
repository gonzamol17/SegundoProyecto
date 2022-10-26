import unittest
from pytest_bdd import scenarios, given, when, then
from colorama import Fore, Back, Style
from POM.Pages.LandingPage import LandingPage
from POM.Pages.LoginPage import LoginPage
from POM.Pages.MyAccountPage import MyAccountPage
import HtmlTestRunner



AUTOMATION_PAGE = 'https://automationteststore.com/'
scenarios('../features/Login.feature')


@given("I am on the Automation test store page")
def step_Go_Login_Page_of_Automation_Test_Store(browser):
    browser.get(AUTOMATION_PAGE)
    lp = LandingPage(browser)
    lp.click_Go_Login()



@when('enter a value in "<username>" and "<password>"')
def step_Complete_User_Pass(browser, username, password):
    logpa = LoginPage(browser)
    logpa.do_Login(username, password)
    print(Fore.BLUE+"Account of "+ username)



@then("I can verify that I am in my account")
def step_CheckMyAccount(browser):
    account = MyAccountPage(browser)
    x = account.verificar_Ingreso_Correcto2()
    print(x)
    assert x == 'MY ACCOUNT'
    print("Estoy dentro de la página de My account")


@then('I check if I can enter my account and "<message>"')
def step_verifyMyaccount(browser, message):
    account = MyAccountPage(browser)
    logpa = LoginPage(browser)
    # x = account.verificar_Ingreso_Correcto2()
    #print(x)
    #assert x == 'MY ACCOUNT'
    #print(message)

    try:
        x = account.verificar_Ingreso_Correcto2()
        assert x == 'MY ACCOUNT'
        print(message)
    except:
        x = logpa.show_error_username_password()
        assert x == '×\nError: Incorrect login or password provided.'
        print(message)



if __name__ == '__main__':
     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\admin\\PycharmProjects\\SegundoProyecto\\Reports'), verbosity=2)
