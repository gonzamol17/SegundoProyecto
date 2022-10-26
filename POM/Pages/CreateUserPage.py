from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class CreateUserPageLocators():

    label_first_name = (By.ID, "AccountFrm_firstname")
    label_last_name = (By.ID, "AccountFrm_lastname")
    label_email = (By.ID, "AccountFrm_email")
    label_address_1 = (By.ID, "AccountFrm_address_1")
    label_city = (By.ID, "AccountFrm_city")
    drop_down_region = (By.ID, "AccountFrm_zone_id")
    label_zip_code = (By.ID, "AccountFrm_postcode")
    drop_down_country = (By.ID, "AccountFrm_country_id")
    label_create_user_name = (By.ID, "AccountFrm_loginname")
    label_create_password = (By.ID, "AccountFrm_password")
    label_confirm_password = (By.ID, "AccountFrm_confirm")
    check_box_suscribe = (By.ID, "AccountFrm_newsletter0")
    check_box_policy = (By.ID, "AccountFrm_agree")
    btn_continue_register2 = (By.CSS_SELECTOR, "#AccountFrm>div.form-group>div>div>button")
    btn_continue_register3 = (By.CSS_SELECTOR, "#maincontainer>div>div.col-md-9.col-xs-12.mt20>div>div>section>a")


    #locators para cuando no ingreso alguno o ninguno de los campos mandatorios
    label_mandatory_field = (By.CSS_SELECTOR, "#maincontainer>div>div>div>div.alert.alert-error.alert-danger")
    label_mandatory_First_Name = (By.CSS_SELECTOR, "#AccountFrm>div:nth-child(5)>fieldset>div:nth-child(1)>span")
    label_mandatory_Last_Name = (By.CSS_SELECTOR, "#AccountFrm>div:nth-child(5)>fieldset>div:nth-child(2)>span")
    label_mandatory_Email = (By.CSS_SELECTOR, "#AccountFrm>div:nth-child(5)>fieldset>div:nth-child(3)>span")
    label_mandatory_Address1 = (By.CSS_SELECTOR, "#AccountFrm>div:nth-child(7)>fieldset>div:nth-child(2)>span")
    label_mandatory_City = (By.CSS_SELECTOR, "#AccountFrm>div:nth-child(7)>fieldset>div:nth-child(4)>span")
    label_mandatory_Region = (By.CSS_SELECTOR, "#AccountFrm>div:nth-child(7)>fieldset>div:nth-child(5)>span")
    label_mandatory_Zipcode = (By.CSS_SELECTOR, "#AccountFrm>div:nth-child(7)>fieldset>div:nth-child(6)>span")
    label_mandatory_Login_Name = (By.CSS_SELECTOR, "#AccountFrm>div:nth-child(9)>fieldset>div:nth-child(1)>span")
    label_mandatory_Password = (By.CSS_SELECTOR, "#AccountFrm>div:nth-child(9)>fieldset>div:nth-child(2)>span")

    #locator para cuando quiero crear una cuenta de un usuario ya existente
    label_existing_user = (By.CSS_SELECTOR, "#maincontainer>div>div>div>div.alert.alert-error.alert-danger")


class CreateUserPage():

    def __init__(self, driver):
        self.driver = driver

    def complete_All_Field_For_New_Account(self, firstname, lastname, email, address, city, zip, login_name, create_pass, confirm_pass):
        self.driver.find_element(*CreateUserPageLocators.label_first_name).send_keys(firstname)
        self.driver.find_element(*CreateUserPageLocators.label_last_name).send_keys(lastname)
        self.driver.find_element(*CreateUserPageLocators.label_email).send_keys(email)
        self.driver.find_element(*CreateUserPageLocators.label_address_1).send_keys(address)
        self.driver.find_element(*CreateUserPageLocators.label_city).send_keys(city)
        self.driver.find_element(*CreateUserPageLocators.label_zip_code).send_keys(zip)
        self.driver.find_element(*CreateUserPageLocators.label_create_user_name).send_keys(login_name)
        self.driver.find_element(*CreateUserPageLocators.label_create_password).send_keys(create_pass)
        self.driver.find_element(*CreateUserPageLocators.label_confirm_password).send_keys(confirm_pass)
        self.driver.find_element(*CreateUserPageLocators.check_box_suscribe).click()
        self.driver.find_element(*CreateUserPageLocators.check_box_policy).click()


    def create_Country(self, country):
        sel = Select(self.driver.find_element(*CreateUserPageLocators.drop_down_country))
        sel.select_by_visible_text(country)

    def create_Region(self, region):
        sel = Select(self.driver.find_element(*CreateUserPageLocators.drop_down_region))
        sel.select_by_visible_text(region)

    def submit_Button_Continue_whitout_Mandatory_field(self):
        self.driver.find_element(*CreateUserPageLocators.btn_continue_register2).click()

    #acá van todos los métodos para los mensajes de alerta
    def show_error_Mandatory_Field(self):
        return self.driver.find_element(*CreateUserPageLocators.label_mandatory_field).text

    def show_Mandatory_Field_First_Name(self):
        return self.driver.find_element(*CreateUserPageLocators.label_mandatory_First_Name).text

    def show_Mandatory_Field_Last_Name(self):
        return self.driver.find_element(*CreateUserPageLocators.label_mandatory_Last_Name).text

    def show_Mandatory_Field_Email(self):
        return self.driver.find_element(*CreateUserPageLocators.label_mandatory_Email).text

    def show_Mandatory_Field_Address(self):
        return self.driver.find_element(*CreateUserPageLocators.label_mandatory_Address1).text

    def show_Mandatory_Field_City(self):
        return self.driver.find_element(*CreateUserPageLocators.label_mandatory_City).text

    def show_Mandatory_Field_Region(self):
        return self.driver.find_element(*CreateUserPageLocators.label_mandatory_Region).text

    def show_Mandatory_Field_Zipcode(self):
        return self.driver.find_element(*CreateUserPageLocators.label_mandatory_Zipcode).text

    def show_Mandatory_Field_LoginName(self):
        return self.driver.find_element(*CreateUserPageLocators.label_mandatory_Login_Name).text

    def show_Mandatory_Field_Password(self):
        return self.driver.find_element(*CreateUserPageLocators.label_mandatory_Password).text

    #método para ver un usuario ya existente
    def show_Existing_User_Message(self):
        return self.driver.find_element(*CreateUserPageLocators.label_existing_user).text
