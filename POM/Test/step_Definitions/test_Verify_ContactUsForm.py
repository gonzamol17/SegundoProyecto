import time
import unittest
from pytest_bdd import scenarios, parsers, given, when, then, scenario
from colorama import Fore, Back, Style
from POM.Pages.LandingPage import LandingPage
from POM.Pages.LoginPage import LoginPage
from POM.Pages.MyAccountPage import MyAccountPage
from POM.Pages.ContactUsPage import ContactUsPage
import HtmlTestRunner



AUTOMATION_PAGE = 'https://automationteststore.com/'
scenarios('../features/Verify_ContactUsForm.feature')

@given("I am on the Automation test logged in")
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



@when("I select the Contact Us option in the footer of the page")
def step_SendRequest(browser):
    account = MyAccountPage(browser)
    account.seleccionar_ContactUs_Option()
    time.sleep(2)
    cu = ContactUsPage(browser)
    print(cu.verificar_ContactUs_Form())
    time.sleep(2)
    assert cu.verificar_ContactUs_Form() == "Contact Us Form"
    print(Fore.GREEN + "Estoy en la página de Contact Us")


@when(parsers.parse('Fill form name "{name}", email "{email}", Enquiry "{message}"'))
def step_FillForm(browser, name, email, message):
    cu = ContactUsPage(browser)
    time.sleep(2)
    cu.fill_FirstName(name)
    time.sleep(2)
    cu.fill_Email(email)
    time.sleep(2)
    cu.fill_Enquiry(message)
    time.sleep(2)
    cu.sendForm()



@then("I want to verify that my question has been sent successfully")
def step_Verify_successful_Sending_Request(browser):
    cu = ContactUsPage(browser)
    message = cu.Verify_Enquiry_Success()
    assert message == "Your enquiry has been successfully sent to the store owner!"
    print(Fore.GREEN + "El formulario se ha enviado exitosamente")



@when("I do not complete any of the fields")
def step_EmptyFields(browser):
    cu = ContactUsPage(browser)
    cu.sendForm()

@then("I want to verify that the validation errors are displayed in each of the fields")
def step_VerifyErrorValidation(browser):
    cu = ContactUsPage(browser)
    name = cu.get_FirstName()
    email = cu.get_Email()
    enquiry = cu.get_Enquiry()
    assert name == "First name: is required field! Name must be between 3 and 32 characters!"
    assert email == "Email: is required field! E-Mail Address does not appear to be valid!"
    assert enquiry == "Enquiry: is required field! Enquiry must be between 10 and 3000 characters!"

    print("Todos los mensajes de validación de campos mandatorios se están mostrando")
    print(Fore.RED + "\n" + name)
    print(Fore.RED + "\n" + email)
    print(Fore.RED + "\n" + enquiry)
    print("El formulario no ha podido ser enviado")

    if __name__ == '__main__':
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
            output='C:\\Users\\admin\\PycharmProjects\\SegundoProyecto\\Reports'), verbosity=2)
