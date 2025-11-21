import time
import unittest
from pytest_bdd import scenarios, parsers, given, when, then, scenario
from POM.Pages.LandingPage import LandingPage
from POM.Pages.LoginPage import LoginPage
from POM.Pages.MyAccountPage import MyAccountPage
from POM.Pages.ShampooPage import ShampooPage

scenarios('../features/Verify_Review.feature')

@given("I am on login in the Automation test")
def step_login(test_setup):
    time.sleep(2)
    # ir a login page
    lp = LandingPage(test_setup)
    lp.click_Go_Login()
    logpa = LoginPage(test_setup)
    time.sleep(2)
    # Esto permite el logueo
    logpa.do_Login("gonza_mol", "Chicharito10")


@when('I select the category, and then the product')
def step_Select_CategoryAndProduct(test_setup):
    my = MyAccountPage(test_setup)
    my.select_HairCare_Shampoo()

@when(parsers.parse('I select the option to give Review to that product, I give it a score, I enter the name of the user "{name}" and a review "{note}".'))
def step_GiveScoreAndReview(test_setup, name, note):
    sp = ShampooPage(test_setup)
    time.sleep(4)
    sp.viewPantene()
    time.sleep(4)
    sp.selectReview()
    time.sleep(4)
    test_setup.execute_script("window.scrollTo(0, 800)")
    sp.setCalification()
    time.sleep(4)
    sp.setName(name)
    time.sleep(4)
    sp.setReview(note)
    time.sleep(4)
    sp.clickSubmitBtn()
    time.sleep(4)

@then("I see the error message, when not completing the code")
def step_GetError(test_setup):
    sp = ShampooPage(test_setup)
    error = sp.errorWithoutCode()
    assert "Human verification has failed! Please try again." in sp.errorWithoutCode()
    print("Al no cargar el código requerido, se está mostrando un mensaje de error: "+sp.errorWithoutCode())

