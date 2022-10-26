import time
import unittest
from pytest_bdd import scenarios, given, when, then
from colorama import Fore, Back, Style
from POM.Pages.LandingPage import LandingPage
from POM.Pages.LoginPage import LoginPage
from POM.Pages.MyAccountPage import MyAccountPage
import HtmlTestRunner




AUTOMATION_PAGE = 'https://automationteststore.com/'


scenarios('../features/Verify_Edit_Manage_Address_Book.feature')


@given("I am on login in the Automation test page")
def step_Login(browser):
    browser.get(AUTOMATION_PAGE)
    lp = LandingPage(browser)
    lp.click_Go_Login()
    time.sleep(2)
    lp = LandingPage(browser)
    lp.click_Go_Login()
    logpa = LoginPage(browser)
    time.sleep(2)
    logpa.do_Login("gonza_mol", "Chicharito10")


@when("I click on the Manage Address Book option, and verify that I have an existing address, editing it and saving that data")
def step_EditAddressBook(browser):
    account = MyAccountPage(browser)
    n = account.getQuantityOfAddressBook()
    assert n != 0
    print(Fore.MAGENTA + "\nSe tiene al menos una dirección ingresada y es: " + Fore.RESET + Fore.GREEN + n + Fore.RESET)
    time.sleep(2)
    account.selectBoxManageAddressBook()
    time.sleep(2)
    account.selectBtnEditAddressBook()
    browser.execute_script("window.scrollTo(0, 500)")
    time.sleep(2)
    account.setAddressTwoAddressBook("Mandioca 2400, 2do Piso")
    time.sleep(3)
    account.saveBtnAddressBook()
    time.sleep(3)


@then("I verify that the system shows me an edited address message, and the new address is within Address Book Entries")
def step_CheckEditedAddress(browser):
    account = MyAccountPage(browser)
    message = account.getAlertMessageAddressBook()
    assert message in "×\nYour address has been successfully updated"
    assert 'rgba(60, 118, 61, 1)' in account.getObjectAlertMessageAddressBook().value_of_css_property('color')
    time.sleep(3)
    print(Fore.MAGENTA + "Se muestra el mensaje y color correcto de dirección editada " +Fore.GREEN+message[2:44]+Fore.RESET)
    time.sleep(2)
    print(Fore.MAGENTA + "Toda la información editada que se tiene de Address Book Entries es: \n" + account.getAllAddressBook())
    assert "Mandioca 2400, 2do Piso" in account.getAllAddressBook()
    print("La nueva segunda dirección editada/agregada, está dentro de Address Book Entries correctamente")
    time.sleep(2)


if __name__ == '__main__':
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
            output='C:\\Users\\admin\\PycharmProjects\\SegundoProyecto\\Reports'), verbosity=2)
