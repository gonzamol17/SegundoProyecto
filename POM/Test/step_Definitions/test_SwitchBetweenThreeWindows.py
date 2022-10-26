import time
import unittest
from pytest_bdd import scenarios, parsers, given, when, then, scenario
from POM.Pages.MyAccountPage import MyAccountPage
import HtmlTestRunner




AUTOMATION_PAGE = 'https://automationteststore.com/'


scenarios('../features/Verify_SwitchBetweenThreeWindows.feature')


@given("I am in the Automation test store")
def step_GoAutomationTestPage(browser):
    browser.get(AUTOMATION_PAGE)
    time.sleep(2)

@when("I click on two components of the web and two new tabs open", target_fixture='long')
def step_opennewtabs(browser):
    browser.execute_script("window.scrollTo(0, 4000)")
    time.sleep(2)
    account = MyAccountPage(browser)
    print("\nEl título de la Tab principal es: "+browser.title)
    assert browser.title == "A place to practice your automation skills!"
    account.selectBtnContribute()
    account.selectLinkAbanteCard()
    # este driver.window_handles, devuelve la lista de todas las ventanas abiertas hasta el momento
    windows = browser.window_handles
    print("Los Id's de las ventanas abiertas son: " + str(windows))
    long = len(windows)
    print("La cantidad de ventanas abiertas es: " + str(long))
    return long


@then("I capture the title of each page and the url, I close the tabs and go back to the original tab showing the title")
def step_CaptureTitleAndUrlAndCloseTabs(long, browser):
    aux = long - 1
    while aux >= 1:
        browser.switch_to.window(browser.window_handles[aux])
        print("La url de la tab " + str(aux) + " es: " + browser.current_url)
        print("El título de tab " + str(aux) + " es: " + browser.title)
        assert browser.current_url == "https://www.abantecart.com/" or browser.current_url == "https://www.abantecart.com/contribute-to-abantecart"
        aux = aux - 1
        time.sleep(2)
        browser.close()

    time.sleep(2)
    browser.switch_to.window(browser.window_handles[aux])
    print("Estoy de vuelta en la tab " + str(aux) + " y el título es: " + browser.title)
    print("La url de la tab " + str(aux) + " es: " + browser.current_url)
    assert browser.current_url == "https://automationteststore.com/"
    time.sleep(2)



if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='C:\\Users\\admin\\PycharmProjects\\SegundoProyecto\\Reports'), verbosity=2)

