import time
import unittest
from pytest_bdd import scenarios, parsers, given, when, then, scenario
from POM.Pages.LandingPage import LandingPage
from POM.Pages.LoginPage import LoginPage
from POM.Pages.MyAccountPage import MyAccountPage
from POM.Pages.ShampooPage import ShampooPage
import HtmlTestRunner


AUTOMATION_PAGE = 'https://automationteststore.com/'


scenarios('../features/Verify_Review.feature')


@given("I am on login in the Automation test")
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


@when('I select the category, and then the product')
def step_Select_CategoryAndProduct(browser):
    my = MyAccountPage(browser)
    my.select_HairCare_Shampoo()

@when(parsers.parse('I select the option to give Review to that product, I give it a score, I enter the name of the user "{name}" and a review "{note}".'))
def step_GiveScoreAndReview(browser, name, note):
    sp = ShampooPage(browser)
    time.sleep(4)
    sp.viewPantene()
    time.sleep(4)
    sp.selectReview()
    time.sleep(4)
    browser.execute_script("window.scrollTo(0, 800)")
    sp.setCalification()
    time.sleep(4)
    sp.setName(name)
    time.sleep(4)
    sp.setReview(note)
    time.sleep(4)
    sp.clickSubmitBtn()
    time.sleep(4)

@then("I see the error message, when not completing the code")
def step_GetError(browser):
    sp = ShampooPage(browser)
    error = sp.errorWithoutCode()
    assert "Human verification has failed! Please try again." in sp.errorWithoutCode()
    print("Al no cargar el código requerido, se está mostrando un mensaje de error: "+sp.errorWithoutCode())




if __name__ == '__main__':
     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\admin\\PycharmProjects\\SegundoProyecto\\Reports'), verbosity=2)

