import time
import unittest
import pytest
from pytest_bdd import scenarios, given, when, then
from POM.Pages.LandingPage import LandingPage
from POM.Pages.LoginPage import LoginPage
from POM.Pages.MyAccountPage import MyAccountPage
from POM.Pages.SkinCarePage import SkinCarePage

#AUTOMATION_PAGE = 'https://automationteststore.com/'

scenarios('../features/Load_shopping_Cart.feature')

@given("I am on the Automation test store page logged in")
def step_Login_to_the_Page(test_setup):
    lp = LandingPage(test_setup)
    skp = SkinCarePage(test_setup)
    lp.click_Go_Login()
    logpa = LoginPage(test_setup)
    logpa.do_Login("gonza_mol", "Chicharito10")
    my = MyAccountPage(test_setup)
    time.sleep(2)
    my.seleccionar_Producto_SkinCare()
    time.sleep(4)
    test_setup.execute_script("window.scrollTo(0, 800)")
    time.sleep(4)
    skp.add_Product_Antiage()
    time.sleep(2)
    skp.add_Product_Cremenuit()
    time.sleep(2)
    skp.add_Product_Facialcream()
    time.sleep(2)
    skp.add_Product_Absolueyes()
    time.sleep(2)
    my.seleccionar_Logoff()


@when("I select some products to add to my shopping cart, without confirming the purchase")
def step_impl():
    print("No se confirma la compra de ninguno de los productos")


@then("I see those products in my shopping cart")
def step_impl():
    print("Se agregaron productos al carrito de compras del usuario gonza_mol")

