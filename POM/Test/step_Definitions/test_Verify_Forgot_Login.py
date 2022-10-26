import time
import unittest
from pytest_bdd import scenarios, parsers, given, when, then, scenario
from colorama import Fore, Back, Style

from POM.Pages.ForgotLoginPage import ForgotLoginPage
from POM.Pages.LandingPage import LandingPage
from POM.Pages.LoginPage import LoginPage
from POM.Pages.MyAccountPage import MyAccountPage
from POM.Pages.ShoppingCartPage import ShoppingCartPage
from POM.Pages.ShampooPage import ShampooPage
import HtmlTestRunner


AUTOMATION_PAGE = 'https://automationteststore.com/'
scenarios('../features/Verify_Forgot_Login.feature')

@given("I try to enter the Automation test store page, and I don't remember the password")
def step_GoLoginPage(browser):
    browser.get(AUTOMATION_PAGE)
    time.sleep(2)
    lp = LandingPage(browser)
    lp.click_Go_Login()

@when('I select the forgot password option, and lastname "<lastname>" and email "<email>"')
def step_ForgotLoginPageAndComplete(browser, lastname, email):
    lp = LandingPage(browser)
    flp = ForgotLoginPage(browser)
    lp.selectForgotLogin()
    flp.set_LastName(lastname)
    flp.set_Email(email)
    flp.selectBtnContinue()

@then('I get a message with result "<message>" for password recovery')
def step_GetResults(browser):
    flp = ForgotLoginPage(browser)
    try:
        if ("rgba(223, 240, 216, 1)" == flp.getAlertSuccessMessage().value_of_css_property('background-color')):
           assert "Success: Your login name reminder has been sent to your e-mail address." in flp.getTextSuccesfullMessageAlert()
           print(Fore.GREEN + "Se está visualizando el mensaje de Alerta exitoso" + Fore.RESET)
           assert "rgba(223, 240, 216, 1)" == flp.getAlertSuccessMessage().value_of_css_property('background-color')
           print(Fore.GREEN + "El color de la alerta es el verde esperado" + Fore.RESET)
           flp.selecteIconCloseAlert()
           try:
             if flp.getAlertSuccessMessage().is_displayed():
                print("Se sigue verificando el alerta exitoso, y no debería aparecer")
           except:
              print(Fore.GREEN + "Ya no se está visualizando el alerta exitoso, de acuerdo a lo esperado, porque fue cerrado" + Fore.RESET)

    except:
        assert "Error: No records found matching information your provided" in flp.getTextFailedMessageAlert()
        print(Fore.RED + "Se está visualizando el mensaje de Alerta fallido" + Fore.RESET)
        assert "rgba(242, 222, 222, 1)" == flp.getAlertFailedMessage().value_of_css_property('background-color')
        print(Fore.RED + "El color de la alerta es el rojo esperado" + Fore.RESET)
        flp.selecteIconCloseAlertFailed()
        try:
            if flp.getAlertFailedMessage().is_displayed():
                print("Se sigue verificando el alerta fallido, y no debería aparecer")
        except:

            print(
                Fore.RED + "Ya no se está visualizando el alerta exitoso, de acuerdo a lo esperado, porque fue cerrado" + Fore.RESET)