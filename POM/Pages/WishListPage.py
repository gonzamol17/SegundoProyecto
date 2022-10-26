from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains


class WishlistPageLocators():
      label_product_selected1 = (By.CSS_SELECTOR, "tbody>tr.wishlist_59>td:nth-child(2)>a")

class WishListPage():

    def __init__(self, driver):
        self.driver = driver

    def verify_product_added(self):
        return self.driver.find_element(*WishlistPageLocators.label_product_selected1).text