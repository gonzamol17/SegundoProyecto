import re
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
from POM.Pages.CheckoutConfirmationPage import CheckoutConfirmationPage
from POM.Pages.My_Order_History import My_Order_History
import HtmlTestRunner



AUTOMATION_PAGE = 'https://automationteststore.com/'


scenarios('../features/Verify_Order_Id.feature')


@given("I am on the Automation test store page logged in, with zero products")
def step_login(browser):
    browser.get(AUTOMATION_PAGE)
    time.sleep(2)
    # ir a login page
    lp = LandingPage(browser)
    lp.click_Go_Login()
    logpa = LoginPage(browser)
    time.sleep(2)
    # Esto permite el logueo
    logpa.do_Login("gonza_mol", "Chicharito10")


@when("I select the type of product and its characteristics, confirm the order, and I save the order_id")
def step_Confirm_Order(browser):
    # Acá selecciono La pagina del producto(lapiz labial) para agregarlo a carrito e ir a la pagina de producto
    scp = ShoppingCartPage(browser)
    my = MyAccountPage(browser)
    my.seleccionar_Producto_Makeup()
    time.sleep(2)
    lip = LipsPage(browser)
    lip.add_Cart1()
    time.sleep(2)

    # Acá creo un objeto del  tipo de producto elegido, y selecciono el color, y la cantidad y verifico que coincido lo que pido
    pp = ProductPage(browser)
    pp.select_Product_Lips_Color_And_Qty("Viva Glam II", "1")
    time.sleep(2)
    scp.do_Checkout()
    time.sleep(2)



@then("I verify that the order was processed successfully and i checked the Order_id on a Order History section")
def step_Search_Order_Id(browser):
    time.sleep(2)
    # Acá creo un objeto del tipo checkoutconfirmationpage
    ccp = CheckoutConfirmationPage(browser)
    # con este botón ya confirmo el pedido
    ccp.do_Checkout_Confirmation()
    time.sleep(2)
    Order_id = ccp.show_Order_Id()
    #aux = Order_id[11:16]
    #print(aux)
    Order_number = re.findall("[0-9]", Order_id)
    Only_order_id = ''.join(Order_number)
    print(Only_order_id)

    #Acá voy a ir a Order history y busco mi order_id recientemente creado
    ccp.Select_Order_History_Option()
    moh = My_Order_History(browser)
    #print(moh.Verify_Order_History())
    #aux1 = moh.Verify_Order_History()[10:15]
    aux1 = moh.Verify_Order_History()
    assert Only_order_id in aux1
    print(Fore.GREEN+ "El id de la orden recientemente obtenida, coincide con el id último de mi historial, y es: "+moh.Verify_Order_History())



if __name__ == '__main__':
     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\admin\\PycharmProjects\\SegundoProyecto\\Reports'), verbosity=2)


