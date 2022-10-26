import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class My_Order_HistoryLocators():
      label_order_id_history = (By.CSS_SELECTOR, "#maincontainer>div>div.col-md-9.col-xs-12.mt20>div>div>div:nth-child(1)>div:nth-child(1)")



class My_Order_History():

    def __init__(self, driver):
        self.driver = driver


    def Verify_Order_History(self):
        return self.driver.find_element(*My_Order_HistoryLocators.label_order_id_history).text