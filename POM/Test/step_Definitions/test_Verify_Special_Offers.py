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

from POM.Pages.SpecialOffersPage import SpecialOffersPage

AUTOMATION_PAGE = 'https://automationteststore.com/'
scenarios('../features/Verify_Special_Offers.feature')


@given("I am on Automation test page")
def step_GoAutomationTestPage(browser):
    browser.get(AUTOMATION_PAGE)
    time.sleep(2)


@when("I select the Special link")
def step_SelectSpecialLink(browser):
    lp = LandingPage(browser)
    lp.selectSpecialsOffers()
    so = SpecialOffersPage(browser)
    numberofsales = len(so.getAllSales())
    print(Fore.YELLOW + "\nCantidad de elementos en sales es: " + str(numberofsales) + Fore.RESET)
    aux = so.getAllSales()
    browser.execute_script("window.scrollTo(0, 500)")
    time.sleep(2)


@then("I should see the number of specials products, and if they have the Sale tag")
def step_CountSpecialProductAndCheckTagSale(browser):
    so = SpecialOffersPage(browser)
    aux = so.getAllSales()
    n = 1
    b = 6
    for i in aux:
        try:
            if n <= 4:
                assert so.getIndividualSpecialText(n).is_displayed()
                print(Fore.GREEN + "Se está visualizando el label de Sale en el producto: " + str(n) + Fore.RESET)
                print(so.getIndividualSpecialText(n).is_displayed())
                n = n + 1
            else:
                time.sleep(2)
                assert so.getIndividualSpecialText(b).is_displayed()
                print(Fore.GREEN + "Se está visualizando el label de Sale en el producto: " + str(b - 1) + Fore.RESET)
                print(so.getIndividualSpecialText(b).is_displayed())
                b = b + 1

        except:
            print(Fore.RED + "En alguno de los productos, el label Sales, no se está visualizando" + Fore.RESET)


