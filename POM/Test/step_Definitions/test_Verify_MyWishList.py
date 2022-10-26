import time
import unittest
from pytest_bdd import scenarios, given, when, then
from colorama import Fore, Back, Style
from POM.Pages.LandingPage import LandingPage
from POM.Pages.LoginPage import LoginPage
from POM.Pages.MyAccountPage import MyAccountPage
from POM.Pages.LipsPage import LipsPage
from POM.Pages.ProductPage import ProductPage
from POM.Pages.ShoppingCartPage import ShoppingCartPage
from POM.Pages.WishListPage import WishListPage
import HtmlTestRunner



AUTOMATION_PAGE = 'https://automationteststore.com/'
scenarios('../features/Verify_MyWishList.feature')

@given("I am on the Automation test store logged in")
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


@when("I select a product and add it to my wish list")
def step_AddProduct(browser):
    scp = ShoppingCartPage(browser)
    my = MyAccountPage(browser)
    my.seleccionar_Producto_Makeup()
    time.sleep(2)
    lip = LipsPage(browser)
    time.sleep(4)
    lip.select_LipsProduct()
    time.sleep(2)
    # Acá creo un objeto del  tipo de producto elegido, y selecciono el color, y la cantidad y verifico que coincido lo que pido
    pp = ProductPage(browser)
    time.sleep(5)
    time.sleep(3)
    try:
        pp.Add_Wish_List()

    except:
        pp.Remove_Wish_List()
        pp.Add_Wish_List()

    time.sleep(3)
    pp.Add_Wish_List()
    time.sleep(5)

@then("I enter on My Wish List section, and verify that the product is added")
def step_VerifyMyWishList(browser):
    pp = ProductPage(browser)
    product = pp.verify_Existing_Product()
    lp = LandingPage(browser)
    lp.Select_My_Wish_List_Option()
    wl = WishListPage(browser)
    assert product == wl.verify_product_added()
    print(Fore.GREEN+"El producto seleccionado "+product+" coincide con el de Mi lista de deseos  "+wl.verify_product_added())

if __name__ == '__main__':
     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\admin\\PycharmProjects\\SegundoProyecto\\Reports'), verbosity=2)

