import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class LipsPageLocators():
    btn_AddCart1 = (By.CSS_SELECTOR, "div:nth-child(2)>div.thumbnail>div.pricetag.jumbotron>a>i")
    btn_Select_Product =(By.CSS_SELECTOR, "div:nth-child(2)>div.thumbnail>a>img")


class LipsPage():

    def __init__(self, driver):
        self.driver = driver


    def add_Cart1(self):
        self.driver.find_element(*LipsPageLocators.btn_AddCart1).click()

    def select_LipsProduct(self):
        self.driver.find_element(*LipsPageLocators.btn_Select_Product).click()


    
