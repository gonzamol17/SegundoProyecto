import time
from colorama import Fore
from pytest_bdd import scenarios, given, when, then
from POM.Pages.MyAccountPage import MyAccountPage

AUTOMATION_PAGE = 'https://automationteststore.com/'


scenarios('../features/Verify_OrderByName.feature')


@given("I am on the Automation page")
def step_GoAutomationPage(browser):
    browser.get(AUTOMATION_PAGE)
    time.sleep(2)

@when('select the Books-Paperback products and select sort by "<criteria>"')
def step_SelectProductandSortCriteria(browser, criteria):
    my = MyAccountPage(browser)
    my.seleccionar_Producto_Books_Paperback()
    time.sleep(2)
    my.selectOrderByNameA_Z(criteria)


@then("I verify that the products are ordered by the chosen criteria")
def step_VerifyOrderOfProducts(browser):
    lista1 = ["BLLEGIANT BY VERONICA ROTH", "PAPER TOWNS BY JOHN GREEN",
              "THE MIRACLE MORNING: THE NOT-SO-OBVIOUS SECRET GUARANTEED TO TRANSFORM YOUR LIFE"]
    my = MyAccountPage(browser)
    paper = my.getListOfPaperback()
    name = my.getNameOfPaperback()
    print(Fore.MAGENTA + "\nEl número de paperback en la página es: " + str(len(my.getListOfPaperback())) + Fore.RESET)
    lista2 = []
    n = 0
    b = 0
    for i in name:
        lista2.append(i.text)
        # print(Fore.CYAN+i.text+Fore.RESET)
        if lista2[n] == lista1[n]:
            assert lista2[n] == lista1[n]
            print(Fore.CYAN + i.text + Fore.RESET)
            n = n + 1
        else:
            print(Fore.RED + "Los elementos no están ordenados alfabéticamente" + Fore.RESET)
            b = 1
            break
    if b == 1:
        print(Fore.RED + "No se muestra nada ya que no están ordenados alfabéticamente" + Fore.RESET)
    else:
        print(Fore.GREEN + "Todos los productos están ordenados alfabéticamente (A-Z)" + Fore.RESET)
        print(Fore.GREEN + "El orden de los paperback listados es: " + str(lista2) + Fore.RESET)

