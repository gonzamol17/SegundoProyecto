import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ProductPageLocators():
    list_color = (By.CSS_SELECTOR, "#option305")
    qty = (By.CSS_SELECTOR, "#product_quantity")
    btn_AddCart2 = (By.CSS_SELECTOR, "#product>fieldset>div:nth-child(5)>ul>li>a")
    title_product_searched = (By.CSS_SELECTOR, "#product_details>div>div:nth-child(2)>div>div>h1>span")
    product_not_found = (By.CSS_SELECTOR, "#maincontainer>div>div>div>div>div:nth-child(4)")
    btn_Add_Wish_List = (By.CSS_SELECTOR, "a.wishlist_add.btn.btn-large")
    btn_Remove_Wish_List = (By.CSS_SELECTOR, "#product>fieldset>div.wishlist>a.wishlist_remove.btn.btn-large")
    lbl_Out_of_Stock_Paperback = (By.CSS_SELECTOR, "div.pricetag.jumbotron>span")
    lbl_Paperback_Without_Stock = (By.CSS_SELECTOR, "div:nth-child(2)>div.fixed_wrapper>div>a")

class ProductPage():

    def __init__(self, driver):
        self.driver = driver


    def select_Product_Lips_Color_And_Qty(self, color, qty):
        sel = Select(self.driver.find_element(*ProductPageLocators.list_color))
        sel.select_by_visible_text(color)
        self.driver.find_element(*ProductPageLocators.qty).clear()
        self.driver.find_element(*ProductPageLocators.qty).send_keys(qty)
        self.driver.find_element(*ProductPageLocators.btn_AddCart2).click()


    def verify_Existing_Product(self):
        return self.driver.find_element(*ProductPageLocators.title_product_searched).text

    def verify_Title_Of_Product_Not_Fund (self):
        return self.driver.find_element(*ProductPageLocators.product_not_found).text

    def Add_Wish_List(self):
        self.driver.find_element(*ProductPageLocators.btn_Add_Wish_List).click()

    def Remove_Wish_List(self):
        self.driver.find_element(*ProductPageLocators.btn_Remove_Wish_List).click()

    def getLblOutofStock(self):
        return self.driver.find_element(*ProductPageLocators.lbl_Out_of_Stock_Paperback).text

    def getTitleofPaperbackWithoutStock(self):
        return self.driver.find_element(*ProductPageLocators.lbl_Paperback_Without_Stock).text

    def getObjectOutofStock(self):
        return self.driver.find_element(*ProductPageLocators.lbl_Out_of_Stock_Paperback)
