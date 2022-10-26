import unittest
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from colorama import Fore, Back, Style
from selenium.webdriver.common.keys import Keys


class ContactUsPageLocators():
    label_ContactUsTitle = (By.CSS_SELECTOR, "#ContactUsFrm>h3")
    text_FirstName = (By.CSS_SELECTOR, "#ContactUsFrm_first_name")
    text_Email = (By.ID, "ContactUsFrm_email")
    text_Enquiry = (By.ID, "ContactUsFrm_enquiry")
    btn_SubmitForm = (By.CSS_SELECTOR, "div.col-md-6.col-sm-6>button")
    label_Enquiry_Ok = (By.CSS_SELECTOR, "p:nth-child(3)")
    error_label_FirstName = (By.CSS_SELECTOR, "#field_11>span>div.element_error.has-error")
    error_label_Email = (By.CSS_SELECTOR, "#field_12>span>div.element_error.has-error")
    error_Label_Enquiry = (By.CSS_SELECTOR, "#field_13>span>div.element_error.has-error")


class ContactUsPage():

    def __init__(self, driver):
        self.driver = driver

    def verificar_ContactUs_Form(self):
        return self.driver.find_element(*ContactUsPageLocators.label_ContactUsTitle).text

    def fill_FirstName(self, name):
        self.driver.find_element(*ContactUsPageLocators.text_FirstName).click()
        self.driver.find_element(*ContactUsPageLocators.text_FirstName).send_keys(name)

    def fill_Email(self, email):
        self.driver.find_element(*ContactUsPageLocators.text_Email).click()
        self.driver.find_element(*ContactUsPageLocators.text_Email).send_keys(email)

    def fill_Enquiry(self, message):
        self.driver.find_element(*ContactUsPageLocators.text_Enquiry).click()
        self.driver.find_element(*ContactUsPageLocators.text_Enquiry).send_keys(message)

    def sendForm(self):
        self.driver.find_element(*ContactUsPageLocators.btn_SubmitForm).click()

    def Verify_Enquiry_Success(self):
        return self.driver.find_element(*ContactUsPageLocators.label_Enquiry_Ok).text

    def get_FirstName (self):
        return self.driver.find_element(*ContactUsPageLocators.error_label_FirstName).text

    def get_Email(self):
        return self.driver.find_element(*ContactUsPageLocators.error_label_Email).text

    def get_Enquiry(self):
        return self.driver.find_element(*ContactUsPageLocators.error_Label_Enquiry).text