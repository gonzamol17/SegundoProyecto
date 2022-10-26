from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains


class LandingPageLocators():
    go_Login = (By.CSS_SELECTOR, "#customer_menu_top>li>a")
    label_name = (By.CSS_SELECTOR, "#customer_menu_top>li>a>div")
    label_My_Wish_List = (By.CSS_SELECTOR, "#customer_menu_top>li>ul>li:nth-child(2)>a>i")
    currency_Box = (By.CSS_SELECTOR, "div.container-fluid>div>div.block_6>ul>li>a")
    Euro_Currency = (By.CSS_SELECTOR, "div.block_6>ul>li>ul>li:nth-child(1)>a")
    forgotLogin = (By.CSS_SELECTOR, "#loginFrm>fieldset>a:nth-child(4)")
    specialOffersLink = (By.CSS_SELECTOR, "#main_menu_top>li:nth-child(1)>a>span")

class LandingPage():

    def __init__(self, driver):
        self.driver = driver

    def click_Go_Login(self):
        self.driver.find_element(*LandingPageLocators.go_Login).click()

    def verificar_Nombre_Landing_Page(self):
        return self.driver.find_element(*LandingPageLocators.label_name).text

    def Select_My_Wish_List_Option(self):
        hover = ActionChains(self.driver).move_to_element(self.driver.find_element(*LandingPageLocators.label_name))
        hover.perform()
        self.driver.find_element(*LandingPageLocators.label_My_Wish_List).click()

    def Select_Euro_Currency(self):
        hover = ActionChains(self.driver).move_to_element(self.driver.find_element(*LandingPageLocators.currency_Box))
        hover.perform()
        self.driver.find_element(*LandingPageLocators.Euro_Currency).click()

    def selectForgotLogin(self):
        self.driver.find_element(*LandingPageLocators.forgotLogin).click()

    def selectSpecialsOffers(self):
        self.driver.find_element(*LandingPageLocators.specialOffersLink).click()
