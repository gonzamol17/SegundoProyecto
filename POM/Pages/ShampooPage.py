import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class ShampooPageLocators():
    btn_AddCartBulgary = (By.CSS_SELECTOR, "div:nth-child(1)>div.thumbnail>div.pricetag.jumbotron>a>i")
    lbl_priceBulgary = (By.CSS_SELECTOR, "div:nth-child(1)>div.thumbnail>div.pricetag.jumbotron>div>div")
    btn_AddCartPantene = (By.CSS_SELECTOR, "div:nth-child(2)>div.thumbnail>div.pricetag.jumbotron>a>i")
    lbl_pricePantene = (By.CSS_SELECTOR, "div:nth-child(2)>div.thumbnail>div.pricetag.jumbotron>div>div")
    lbl_titleBulgary = (By.CSS_SELECTOR, "div:nth-child(1)>div.fixed_wrapper>div>a")
    lbl_titlePantene = (By.CSS_SELECTOR, " div:nth-child(2)>div.fixed_wrapper>div>a")
    viewPantene = (By.CSS_SELECTOR, "div:nth-child(2)>div.thumbnail>div.shortlinks>a.details")
    optionViewPantene = (By.CSS_SELECTOR, "div:nth-child(2)>div.thumbnail>a>img")
    optionReview = (By.CSS_SELECTOR, "#myTab>li:nth-child(2)>a")
    optionCalification = (By.CSS_SELECTOR, "#rating4>a")
    lblName = (By.ID, "name")
    lblReview = (By.ID, "text")
    btnSubmit = (By.ID, "review_submit")
    lblError = (By.CSS_SELECTOR, "#review>div.alert.alert-error.alert-danger")

class ShampooPage():

    def __init__(self, driver):
        self.driver = driver



    def add_Fragance(self):
        self.driver.find_element(*ShampooPageLocators.btn_AddCartBulgary).click()

    def get_PriceFragance(self):
        return self.driver.find_element(*ShampooPageLocators.lbl_priceBulgary).text

    def add_Pantene(self):
        self.driver.find_element(*ShampooPageLocators.btn_AddCartPantene).click()

    def get_PricePantene(self):
        return self.driver.find_element(*ShampooPageLocators.lbl_pricePantene).text

    def get_TitleFragance(self):
        return self.driver.find_element(*ShampooPageLocators.lbl_titleBulgary).text

    def get_TitlePantene(self):
        return self.driver.find_element(*ShampooPageLocators.lbl_titlePantene).text

    def viewPantene(self):
        self.driver.find_element(*ShampooPageLocators.optionViewPantene).click()

    def selectReview(self):
        self.driver.find_element(*ShampooPageLocators.optionReview).click()

    def setCalification(self):
        self.driver.find_element(*ShampooPageLocators.optionCalification).click()

    def setName(self, name):
        self.driver.find_element(*ShampooPageLocators.lblName).send_keys(name)

    def setReview(self, note):
        self.driver.find_element(*ShampooPageLocators.lblReview).send_keys(note)

    def clickSubmitBtn(self):
        self.driver.find_element(*ShampooPageLocators.btnSubmit).click()

    def errorWithoutCode(self):
        return self.driver.find_element(*ShampooPageLocators.lblError).text