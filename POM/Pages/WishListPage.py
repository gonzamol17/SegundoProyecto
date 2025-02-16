from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains


class WishlistPageLocators():
<<<<<<< HEAD
      label_product_selected1 = (By.CSS_SELECTOR, "tbody>tr.wishlist_108>td:nth-child(2)>a")
=======
      label_product_selected1 = (By.XPATH, "//a[contains(text(),'LE ROUGE ABSOLU')]")
>>>>>>> 2fa78c339105440924a5bb0d77d85a97438def7b

class WishListPage():

    def __init__(self, driver):
        self.driver = driver

    def verify_product_added(self):
        return self.driver.find_element(*WishlistPageLocators.label_product_selected1).text