import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class CheckoutConfirmationLocators():
    btn_confirm_order = (By.ID, "checkout_btn")

    #para verificar todos los elementos en la páginaCheckoutConfirmationpage
    label_title = (By.CSS_SELECTOR, "#maincontainer>div>div.col-md-9.col-xs-12.mt20>div>h1>span.maintext")
    label_subtitle = (By.CSS_SELECTOR, "div.col-md-9.col-xs-12.mt20>div>div.contentpanel>h4:nth-child(2)")
    label_name_shipping = (By.CSS_SELECTOR, "table.table.confirm_shippment_options>tbody>tr>td:nth-child(1)")
    label_address_shipping = (By.CSS_SELECTOR, "table.table.confirm_shippment_options>tbody>tr>td:nth-child(2)")
    label_flat_shipping = (By.CSS_SELECTOR, "table.table.confirm_shippment_options>tbody>tr>td:nth-child(3)")
    label_order_summary = (By.CSS_SELECTOR, "div.column_right.col-md-3.col-xs-12.mt20>div.sidewidt>h2>span")
    label_qty_color = (By.CSS_SELECTOR, "table:nth-child(2)>tbody>tr>td.align_left.valign_top")
    label_unit_price = (By.CSS_SELECTOR, "table:nth-child(2)>tbody>tr>td.align_right.valign_top>b")
    label_sub_total = (By.CSS_SELECTOR, "table:nth-child(5)>tbody>tr:nth-child(1)>td:nth-child(2)>span")
    label_flat_shipping_rate = (By.CSS_SELECTOR, "table:nth-child(5)>tbody>tr:nth-child(2)>td:nth-child(2)>span")
    label_total = (By.CSS_SELECTOR, "table:nth-child(5)>tbody>tr:nth-child(3)>td:nth-child(2)>span")
    label_payment_title = (By.CSS_SELECTOR, "div.col-md-9.col-xs-12.mt20>div>div.contentpanel>h4:nth-child(4)")
    label_name_payment = (By.CSS_SELECTOR, "table.table.confirm_payment_options>tbody>tr>td:nth-child(1)")
    label_address_payment = (By.CSS_SELECTOR, "table.table.confirm_payment_options>tbody>tr>td:nth-child(2)")
    label_cash_delivery = (By.CSS_SELECTOR, "table.table.confirm_payment_options>tbody>tr>td:nth-child(3)")
    label_order_id = (By.CSS_SELECTOR, "#maincontainer>div>div>div>div>section>p:nth-child(3)")
    label_welcome = (By.CSS_SELECTOR, "#customer_menu_top>li>a>div")
    label_order_history = (By.CSS_SELECTOR, "#customer_menu_top>li>ul>li:nth-child(6)>a>i")



class CheckoutConfirmationPage():

    def __init__(self, driver):
        self.driver = driver


    def do_Checkout_Confirmation(self):
        return self.driver.find_element(*CheckoutConfirmationLocators.btn_confirm_order).click()

    def show_Title(self):
        return self.driver.find_element(*CheckoutConfirmationLocators.label_title).text

    def show_Subtitle(self):
        return self.driver.find_element(*CheckoutConfirmationLocators.label_subtitle).text

    def show_Name_Shipping(self):
        return self.driver.find_element(*CheckoutConfirmationLocators.label_name_shipping).text

    def show_Address_Shipping(self):
        return self.driver.find_element(*CheckoutConfirmationLocators.label_address_shipping).text

    def show_Flat_Shipping(self):
        return self.driver.find_element(*CheckoutConfirmationLocators.label_flat_shipping).text

    def show_Order_Summary(self):
        return self.driver.find_element(*CheckoutConfirmationLocators.label_order_summary).text

    def show_Qty_Color(self):
        return self.driver.find_element(*CheckoutConfirmationLocators.label_qty_color).text

    def show_Unit_Price(self):
        return self.driver.find_element(*CheckoutConfirmationLocators.label_unit_price).text

    def show_Sub_Total(self):
        return self.driver.find_element(*CheckoutConfirmationLocators.label_sub_total).text

    def show_Flat_Shipping_Rate(self):
        return self.driver.find_element(*CheckoutConfirmationLocators.label_flat_shipping_rate).text

    def show_Total(self):
        return self.driver.find_element(*CheckoutConfirmationLocators.label_total).text

    def show_Payment_Title(self):
        return self.driver.find_element(*CheckoutConfirmationLocators.label_payment_title).text

    def show_Name_Payment(self):
        return self.driver.find_element(*CheckoutConfirmationLocators.label_name_payment).text

    def show_Address_Payment(self):
        return self.driver.find_element(*CheckoutConfirmationLocators.label_address_payment).text

    def show_Cash_Deliveryt(self):
        return self.driver.find_element(*CheckoutConfirmationLocators.label_cash_delivery).text

    def show_Order_Id(self):
        return self.driver.find_element(*CheckoutConfirmationLocators.label_order_id).text

    def Select_Order_History_Option(self):
        hover = ActionChains(self.driver).move_to_element(self.driver.find_element(*CheckoutConfirmationLocators.label_welcome))
        hover.perform()
        self.driver.find_element(*CheckoutConfirmationLocators.label_order_history).click()