import unittest
from pytest_bdd import scenarios, parsers, given, when, then, scenario
from colorama import Fore, Back, Style
import time
from POM.Pages.LandingPage import LandingPage
from POM.Pages.LoginPage import LoginPage
from POM.Pages.MyAccountPage import MyAccountPage
import HtmlTestRunner


AUTOMATION_PAGE = 'https://automationteststore.com/'


scenarios('../features/Show_Footer_Elements.feature')



@given("That I am logged in, and i want to count and display all elements of the page footer")
def step_logged(browser):
    browser.get(AUTOMATION_PAGE)
    time.sleep(2)
    # ir a login page
    lp = LandingPage(browser)
    lp.click_Go_Login()
    logpa = LoginPage(browser)
    time.sleep(2)
    # Esto permite el logueo
    logpa.do_Login("gonza_mol", "Chicharito10")


@when("I scroll down, to the Footer section of the page")
def step_Scroll_Down(browser):
    browser.execute_script("window.scrollTo(0, 700)")


@then("I can count the elements that make up the footer and show each one")
def step_Count_Footer_Element(browser):
    account = MyAccountPage(browser)
    n = account.contar_Footer_Component()
    print(Fore.BLUE+"la cantidad de elementos en el footer es: "+str(n))
    print(Fore.BLUE+"Los elementos del footer son:")
    m = account.mostrar_Footer_Component()
    aux = 1
    for idx, ele_foo in enumerate(m):
        if aux == 1:
            print(idx, ele_foo.text[0:9])
            aux=2
        else:
            print(idx, ele_foo.text[0:10])



if __name__ == '__main__':
     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\admin\\PycharmProjects\\SegundoProyecto\\Reports'), verbosity=2)
