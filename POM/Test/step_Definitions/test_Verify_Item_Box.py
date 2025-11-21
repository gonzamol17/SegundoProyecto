import time
import unittest
from pytest_bdd import scenarios, parsers, given, when, then, scenario
from colorama import Fore, Back, Style
from POM.Pages.LandingPage import LandingPage
from POM.Pages.LoginPage import LoginPage
from POM.Pages.MyAccountPage import MyAccountPage
from POM.Pages.ShoppingCartPage import ShoppingCartPage
from POM.Pages.ShampooPage import ShampooPage

scenarios('../features/Verify_Item_Box.feature')

@given("I am on the Automation test logged")
def step_login(test_setup):
     time.sleep(2)
     # ir a login page
     lp = LandingPage(test_setup)
     lp.click_Go_Login()
     logpa = LoginPage(test_setup)
     time.sleep(2)
     # Esto permite el logueo
     logpa.do_Login("gonza_mol", "Chicharito10")


@when("I change the currency and i select two products with that currency")
def step_ChangeCurrency_SelectProducts(test_setup):
     # Verifico que no tenga nada en el carrito de Compras
     scp = ShoppingCartPage(test_setup)
     lp = LandingPage(test_setup)
     my = MyAccountPage(test_setup)
     my.seleccionar_Cart_Option()

     try:
          assert scp.check_Label_Without_Element() == 'Your shopping cart is empty!\nContinue'
          lp.Select_Euro_Currency()
          my.select_HairCare_Shampoo()
     except:
          # scp.clean_Shopping_Cart()
          print(Fore.RED + "La cantidad de Productos eliminados del carrito fueron: " + str(
               scp.contar_Elementos_Eliminados()))
          scp.clean_List_Of_Products()
          time.sleep(2)
          scp.click_Btn_Continue()
          time.sleep(2)
          lp.Select_Euro_Currency()
          my.select_HairCare_Shampoo()
     time.sleep(4)

@then("selecting the item box, i have to view the two selected products and they are in the changed currency.")
def step_VerifyItemBox(test_setup):
     sp = ShampooPage(test_setup)
     time.sleep(4)
     sp.add_Fragance()
     currencyfrangance = sp.get_PriceFragance()
     titlefragance = sp.get_TitleFragance()
     time.sleep(4)
     sp.add_Pantene()
     currencypantene = sp.get_PricePantene()
     titlepantene = sp.get_TitlePantene()
     test_setup.execute_script("window.scrollTo(0, 400)")
     time.sleep(4)
     my = MyAccountPage(test_setup)
     my.open_ItemBox()
     time.sleep(4)
     productfragance = my.get_TitleFragance()
     productshampoo = my.get_TitleShampoo()

     assert titlefragance == productfragance
     assert titlepantene == productshampoo
     assert "€" in currencypantene
     assert "€" in currencyfrangance
     print(Fore.GREEN + "Se encontraron dos productos en el box de Items")
     print(Fore.GREEN + "Los dos productos encontrados en el box de Item, son los que se seleccionaron anteriormente")
     print(Fore.GREEN + "y ambos precios están en moneda Euro")

