from selenium.webdriver.common.by import By


class SpecialOffersPageLocators():
    allSales = (By.CSS_SELECTOR, "div>div.thumbnail>span")



class SpecialOffersPage():

    def __init__(self, driver):
        self.driver = driver

    #def getSale_Counter(self, num):
     #   return self.driver.find_element(By.CSS_SELECTOR, "div:nth-child("+str(num)+") > div.thumbnail > span")

    def getAllSales(self):
        return self.driver.find_elements(*SpecialOffersPageLocators.allSales)

    def getIndividualSpecialText(self, num):
        return self.driver.find_element(By.CSS_SELECTOR, "div:nth-child("+str(num)+")>div.thumbnail>span")