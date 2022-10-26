import time
from pytest_bdd import scenarios, given, when, then
from colorama import Fore, Back, Style
from POM.Pages.MyAccountPage import MyAccountPage



AUTOMATION_PAGE = 'https://automationteststore.com/'


scenarios('../features/Verify_Testimonials.feature')


@given("I am on the Automation test")
def step_GoAutomationStore(browser):
    browser.get(AUTOMATION_PAGE)
    time.sleep(2)


@when("I scroll to the bottom of the screen, and check each of the items in the Testimonials section", target_fixture='t')
def step_CheckItems(browser):
    account = MyAccountPage(browser)
    browser.execute_script("window.scrollTo(0, 4000)")
    t = account.getTestimonials()
    return t

@then("I verify each existing testimonial, and print them")
def step_VerifyAndPrintTestimonials(t, browser):
    lista1 = ['Sub_cero', '1er', '2do', '3er', '4to', '5to']
    n = 0
    print("\n")
    for test in t:
        if n == 0 or n == 5:
           n = n + 1
        else:
           assert test.text in "Regular customer and products" or "Returns were easy and my" or "I found this store to be very reasonably" or "Really great products"
           print(Fore.GREEN + "El título del " + lista1[n] + " Testimonials es: " + Fore.RESET + test.text)
           n = n + 1
           time.sleep(7)

