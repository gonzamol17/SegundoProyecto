import unittest
from pytest_bdd import scenarios, parsers, given, when, then, scenario
from colorama import Fore, Back, Style
import time
from POM.Pages.LandingPage import LandingPage
from POM.Pages.LoginPage import LoginPage
from POM.Pages.ProductPage import ProductPage
from POM.Pages.MyAccountPage import MyAccountPage
import HtmlTestRunner



AUTOMATION_PAGE = 'https://automationteststore.com/'


scenarios('../features/Find_Product.feature')


@given('I am on login in the Automation test store page, and I want to search for a certain product')
def step_Go_Login_Page_of_Automation_Test_Store(browser):
    browser.get(AUTOMATION_PAGE)
    time.sleep(2)
    # ir a login page
    lp = LandingPage(browser)
    lp.click_Go_Login()
    logpa = LoginPage(browser)
    time.sleep(2)
    # Esto permite el logueo
    logpa.do_Login("gonza_mol", "Chicharito10")



@when(parsers.parse('I type the "{product}" to search in the search engine, and I execute the search with glass'))
def step_Search_Product_With_Glass(browser, product):
    my = MyAccountPage(browser)
    my.seleccionar_Búsqueda(product)
    my.ejecutar_Búsqueda_Glass()



@when(parsers.parse('I type the "{miel}" to search in the search engine, and I execute the search with Enter keys'))
def step_Search_Product_With_Enter(browser, miel):
    my = MyAccountPage(browser)
    my.ejecutar_Búsqueda_Enter(miel)


@then(parsers.parse('I get a product "{pro}" and verify that it is the desired product'))
def step_Verify_Product_French(browser, pro):
    pp = ProductPage(browser)
    
    try:
        name = pp.verify_Existing_Product()
        assert pro in name
        print("Y el titulo encontrado es " + Fore.BLUE + name)

    except:
        print(Fore.BLUE +"No se ha encontrado un título que contenga la palabra buscada")



@then(parsers.parse('I dont get product "{miel}" and verify that it is the desired product'))
def step_Verify_Product_Miel(browser, miel):
    pp = ProductPage(browser)
    #print(pp.verify_Title_Of_Product_Not_Fund())
    name = pp.verify_Title_Of_Product_Not_Fund()
    assert name == 'There is no product that matches the search criteria.'
    print(Fore.BLUE + "El producto buscado no se ha encontrado, en la página, mostrando el siguiente mensaje \n" + name)




if __name__ == '__main__':
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
            output='C:\\Users\\admin\\PycharmProjects\\SegundoProyecto\\Reports'), verbosity=2)


