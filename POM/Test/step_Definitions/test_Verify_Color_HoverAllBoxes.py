import time
from colorama import Fore
from pytest_bdd import scenarios, given, when, then
from selenium.webdriver import ActionChains

from POM.Pages.LandingPage import LandingPage
from POM.Pages.LoginPage import LoginPage
from POM.Pages.MyAccountPage import MyAccountPage

AUTOMATION_PAGE = 'https://automationteststore.com/'


scenarios('../features/Verify_Color_Hover_AllBoxes.feature')


@given("I am logged on the Automation page store")
def step_LoginAutomationPage(browser):
    browser.get(AUTOMATION_PAGE)
    time.sleep(2)
    # ir a login page
    lp = LandingPage(browser)
    lp.click_Go_Login()
    logpa = LoginPage(browser)
    time.sleep(2)
    # Esto permite el logueo
    logpa.do_Login("gonza_mol", "Chicharito10")
    time.sleep(2)


@when("I am in my account and I hover over each of the boxes", target_fixture='r')
def step_DoHover(browser):
    account = MyAccountPage(browser)
    numbox = len(account.getAllBoxes())
    box = account.getAllBoxes()
    print(Fore.GREEN + "\nLa cantidad de boxes en My Account es: " + str(numbox) + Fore.RESET)
    r = account.getIndividualBox(1)
    n = 1
    for i in box:
        aux = account.getIndividualBox(n)
        assert 'rgba(245, 245, 245, 1)' in aux.value_of_css_property('background-color')
        hover = ActionChains(browser).move_to_element(aux)
        hover.perform()
        assert 'rgba(242, 92, 39, 1)' in aux.value_of_css_property('background-color')
        n = n + 1
    return  r


@then("I verify that each box is set in the correct color")
def step_VerifyColor(r, browser):
    print(Fore.GREEN + "\nAl hacer hover sobre cada icono en My Account, se está visualizando el color esperado " + Fore.RESET)
    print(Fore.YELLOW + r.value_of_css_property('background-color') + " Que representa naranja" + Fore.RESET)