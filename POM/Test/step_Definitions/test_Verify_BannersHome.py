import time
from colorama import Fore
from pytest_bdd import scenarios, given, when, then

from POM.Pages.MyAccountPage import MyAccountPage

AUTOMATION_PAGE = 'https://automationteststore.com/'


scenarios('../features/Verify_BannersHome.feature')


@given("I am on the Automation page store")
def step_GoAutomationPage(browser):
    browser.get(AUTOMATION_PAGE)
    time.sleep(2)

@when("I stand on the banners section and check each one")
def step_VerifyBannersHome(browser):
    account = MyAccountPage(browser)
    print(Fore.GREEN + "\ncantidad de banners " + str(len(account.getBannersHome())) + Fore.RESET)
    tit1 = account.getTitleBanner1()
    tit2 = account.getTitleBanner2()
    tit3 = account.getTitleBanner3()
    print(Fore.GREEN + "\nTitulo del primer banner" + Fore.RESET)
    for i in tit1:
        print(i.text)
    assert "REALISTIC ONLINE STORE!" in i.text

    print("\n")
    print(Fore.GREEN + "Titulo del segundo banner" + Fore.RESET)
    for i in tit2:
        time.sleep(3)

        # list2=[]
        # list2.append(i.text)
        print(i.text)
        # assert i.text == "Learn Automation Testing\nTHE RIGHT WAY\nREALISTIC ONLINE STORE!"
    assert "THE REAL WORLD" in i.text

    print("\n")
    print(Fore.GREEN + "Titulo del tercer banner" + Fore.RESET)
    time.sleep(3)
    for i in tit3:
        print(i.text)
        # list3 = []
        # list3.append(i.text)

    assert "70% faster than manual testing" in i.text


@then("I can verify that the banners shown are correct")
def step_ShowCorrectMessage(browser):
    print(Fore.GREEN +"Se están mostrando los banners correctos"+Fore.RESET)


