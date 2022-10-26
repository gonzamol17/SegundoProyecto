import re
import sys
import time
import unittest
from pytest_bdd import scenarios, parsers, given, when, then, scenario
from colorama import Fore, Back, Style
from POM.Pages.LandingPage import LandingPage
from POM.Pages.LoginPage import LoginPage
from POM.Pages.MyAccountPage import MyAccountPage
import HtmlTestRunner



AUTOMATION_PAGE = 'https://automationteststore.com/'


scenarios('../features/Verify_SwitchBetweenTwoWindows.feature')



@given("I am on login in the Automation test store")
def step_Login(browser):
    browser.get(AUTOMATION_PAGE)
    time.sleep(2)
    # ir a login page
    lp = LandingPage(browser)
    lp.click_Go_Login()
    logpa = LoginPage(browser)
    time.sleep(2)
    # Esto permite el logueo
    logpa.do_Login("gonza_mol", "Chicharito10")


@when(parsers.parse('I click on the "{link}" link, and i capture the url and the title of the tab'))
def step_GoNewWindow(browser, link):
    account = MyAccountPage(browser)
    if link.upper() == "F" or link.upper() == "T":
        account.selectLinkFborTw(link)
    else:
        if link.upper()=="L":
            print(Fore.GREEN + "\nEstás eligiendo la opción de Linkedin y no está contemplado, por eso te saco de la ejecución" + Fore.RESET)
            exit(1)
    time.sleep(2)
    browser.switch_to.window(browser.window_handles[1])
    aux1 = browser.current_window_handle
    aux2 = aux1.replace('CDwindow-', ' ')
    Fb = "Facebook"
    Tt = "Twitter"
    if link.upper() == "F":
        red = Fb
    elif link.upper()=="T":
        red = Tt
    print(Fore.GREEN + "\n +++++++++++++++++DATOS PESTAÑA "+red+"++++++++++++++++++++++++++++++++++++++++++++++" + Fore.RESET)
    print("El número de ventana de "+red+" es: " + aux2)
    time.sleep(2)
    print("La url de la ventana de "+red+" es: "+browser.current_url)
    print("El nombre de la Tab de "+red+" es: "+browser.title)

@then("I go back to the initial tab and capture the url and the title of the tab")
def step_GoThePreviousWindow(browser):
    browser.switch_to.window(browser.window_handles[0])
    aux3 = browser.current_window_handle
    aux4 = aux3.replace('CDwindow-', ' ')
    print(Fore.GREEN + "\n+++++++++++++++++DATOS PESTAÑA AUTOMATION TEST STORE+++++++++++++++++++++++++++++++++++" + Fore.RESET)
    print("El número de ventana de Test Automation es: " + aux4)
    print("La url de la ventana de Test Automation es: " + browser.current_url)
    print("El nombre de la Tab de la ventana de Test Automation es: " + browser.title)
    assert browser.title == "My Account"



if __name__ == '__main__':
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
            output='C:\\Users\\admin\\PycharmProjects\\SegundoProyecto\\Reports'), verbosity=2)

