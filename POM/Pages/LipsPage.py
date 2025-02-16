import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class LipsPageLocators():
<<<<<<< HEAD
    btn_AddCart1 = (By.CSS_SELECTOR, "div:nth-child(3)>div.thumbnail>div.pricetag.jumbotron>a>i")
=======
    btn_AddCart1 = (By.CSS_SELECTOR, "#maincontainer div:nth-child(3) div.pricetag.jumbotron > a > i")
>>>>>>> 2fa78c339105440924a5bb0d77d85a97438def7b
    btn_Select_Product =(By.CSS_SELECTOR, "div:nth-child(2)>div.thumbnail>a>img")


class LipsPage():

    def __init__(self, driver):
        self.driver = driver


    def add_Cart1(self):
        self.driver.find_element(*LipsPageLocators.btn_AddCart1).click()

    def select_LipsProduct(self):
        self.driver.find_element(*LipsPageLocators.btn_Select_Product).click()


    
