import time
import unittest
from pytest_bdd import scenarios, parsers, given, when, then, scenario
from POM.Pages.MyAccountPage import MyAccountPage

scenarios('../features/Verify_SwitchBetweenThreeWindows.feature')


@given("I am in the Automation test store")
def step_GoAutomationTestPage(test_setup):
    time.sleep(2)

@when("I click on two components of the web and two new tabs open", target_fixture='long')
def step_opennewtabs(test_setup):
    test_setup.execute_script("window.scrollTo(0, 4000)")
    time.sleep(2)
    account = MyAccountPage(test_setup)
    print("\nEl título de la Tab principal es: "+test_setup.title)
    assert test_setup.title == "A place to practice your automation skills!"
    account.selectBtnContribute()
    account.selectLinkAbanteCard()
    # este driver.window_handles, devuelve la lista de todas las ventanas abiertas hasta el momento
    windows = test_setup.window_handles
    print("Los Id's de las ventanas abiertas son: " + str(windows))
    long = len(windows)
    print("La cantidad de ventanas abiertas es: " + str(long))
    return long


@then("I capture the title of each page and the url, I close the tabs and go back to the original tab showing the title")
def step_CaptureTitleAndUrlAndCloseTabs(long, test_setup):
    aux = long - 1
    while aux >= 1:
        test_setup.switch_to.window(test_setup.window_handles[aux])
        print("La url de la tab " + str(aux) + " es: " + test_setup.current_url)
        print("El título de tab " + str(aux) + " es: " + test_setup.title)
        assert test_setup.current_url == "https://www.abantecart.com/" or test_setup.current_url == "https://www.abantecart.com/contribute-to-abantecart"
        aux = aux - 1
        time.sleep(2)
        test_setup.close()

    time.sleep(2)
    test_setup.switch_to.window(test_setup.window_handles[aux])
    print("Estoy de vuelta en la tab " + str(aux) + " y el título es: " + test_setup.title)
    print("La url de la tab " + str(aux) + " es: " + test_setup.current_url)
    assert test_setup.current_url == "https://automationteststore.com/"
    time.sleep(2)
