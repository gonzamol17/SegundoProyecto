import time
import unittest
from pytest_bdd import scenarios, parsers, given, when, then, scenario
from colorama import Fore, Back, Style
from POM.Pages.LandingPage import LandingPage
from POM.Pages.SpecialOffersPage import SpecialOffersPage
from Utils.BaseClass import BaseClass

scenarios('../features/Verify_Special_Offers.feature')

@given("I am on Automation test page")
def step_GoAutomationTestPage(test_setup):
    time.sleep(2)


@when("I select the Special link")
def step_SelectSpecialLink(test_setup):
    lp = LandingPage(test_setup)
    lp.selectSpecialsOffers()
    so = SpecialOffersPage(test_setup)
    numberofsales = len(so.getAllSales())
    print(Fore.YELLOW + "\nCantidad de elementos en sales es: " + str(numberofsales) + Fore.RESET)
    aux = so.getAllSales()
    test_setup.execute_script("window.scrollTo(0, 500)")
    time.sleep(2)


@then("I should see the number of specials products, and if they have the Sale tag")
def step_CountSpecialProductAndCheckTagSale(test_setup):
    so = SpecialOffersPage(test_setup)
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


