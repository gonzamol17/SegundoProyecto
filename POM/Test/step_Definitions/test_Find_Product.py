import logging

import pytest
from pytest_bdd import scenarios, parsers, given, when, then
from colorama import Fore, Back, Style
import time
from POM.Pages.LandingPage import LandingPage
from POM.Pages.LoginPage import LoginPage
from POM.Pages.ProductPage import ProductPage
from POM.Pages.MyAccountPage import MyAccountPage
from Utils.logger_manager import get_logger

#AUTOMATION_PAGE = 'https://automationteststore.com/'

scenarios('../features/Find_Product.feature')

@given('I am on login in the Automation test store page, and I want to search for a certain product')
def step_Go_Login_Page_of_Automation_Test_Store(test_setup):
    #browser.get(AUTOMATION_PAGE)
    log = get_logger("Test Find Product")
    log.info("Por empezar la ejecución del test")
    time.sleep(2)
    # ir a login page
    lp = LandingPage(test_setup)
    lp.click_Go_Login()
    logpa = LoginPage(test_setup)
    time.sleep(2)
    # Esto permite el logueo
    logpa.do_Login("gonza_mol", "Chicharito10")
    time.sleep(2)

@when(parsers.parse('I type the "{product}" to search in the search engine, and I execute the search with glass'))
def step_Search_Product_With_Glass(test_setup, product):
    my = MyAccountPage(test_setup)
    my.seleccionar_Búsqueda(product)
    my.ejecutar_Búsqueda_Glass()
    time.sleep(2)

@when(parsers.parse('I type the "{miel}" to search in the search engine, and I execute the search with Enter keys'))
def step_Search_Product_With_Enter(test_setup, miel):
    my = MyAccountPage(test_setup)
    my.ejecutar_Búsqueda_Enter(miel)


@then(parsers.parse('I get a product "{pro}" and verify that it is the desired product'))
def step_Verify_Product_French(test_setup, pro):
    pp = ProductPage(test_setup)

    try:
        name = pp.verify_Existing_Product()
        assert pro in name
        print("Y el titulo encontrado es " + Fore.BLUE + name)

    except:
        print(Fore.BLUE +"No se ha encontrado un título que contenga la palabra buscada")


@then(parsers.parse('I dont get product "{miel}" and verify that it is the desired product'))
def step_Verify_Product_Miel(test_setup, miel):
    pp = ProductPage(test_setup)
    #print(pp.verify_Title_Of_Product_Not_Fund())
    name = pp.verify_Title_Of_Product_Not_Fund()
    assert name == 'There is no product that matches the search criteria.'
    print(Fore.BLUE + "El producto buscado no se ha encontrado, en la página, mostrando el siguiente mensaje \n" + name)
