import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class CheckoutStatusLocators():
    message_order_successful = (By.CSS_SELECTOR, "#maincontainer>div>div>div>h1>span.maintext>i")
    btn_order_continue = (By.CSS_SELECTOR, "#maincontainer>div>div>div>div>section>a")
    message_alternative = (By.CSS_SELECTOR, "#maincontainer>div>div>div>div>section>p:nth-child(4)")


class CheckoutStatus():

    def __init__(self, driver):
        self.driver = driver


    def get_Message_Successfully(self):
        return self.driver.find_element(*CheckoutStatusLocators.message_order_successful).text

    def select_Button_Continue(self):
        self.driver.find_element(*CheckoutStatusLocators.btn_order_continue).click()

    def get_Message_Alternative(self):
        return self.driver.find_element(*CheckoutStatusLocators.message_alternative).text


