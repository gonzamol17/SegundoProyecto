import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class SkinCarePageLocators():
    absolueeyes = (By.CSS_SELECTOR, "div:nth-child(2)>div.thumbnail>div.pricetag.jumbotron>a>i")
    facialcream = (By.CSS_SELECTOR, "div:nth-child(3)>div.thumbnail>div.pricetag.jumbotron>a>i")
    cremenuit = (By.CSS_SELECTOR, "div:nth-child(4)>div.thumbnail>div.pricetag.jumbotron>a>i")
    antiage = (By.CSS_SELECTOR, "div:nth-child(6)>div.thumbnail>div.pricetag.jumbotron>a>i")



class SkinCarePage():

    def __init__(self, driver):
        self.driver = driver


    def add_Product_Antiage(self):
        self.driver.find_element(*SkinCarePageLocators.antiage).click()

    def add_Product_Absolueyes(self):
        self.driver.find_element(*SkinCarePageLocators.absolueeyes).click()

    def add_Product_Facialcream(self):
        self.driver.find_element(*SkinCarePageLocators.facialcream).click()

    def add_Product_Cremenuit(self):
        self.driver.find_element(*SkinCarePageLocators.cremenuit).click()

