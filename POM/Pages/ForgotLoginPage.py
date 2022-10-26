from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class ForgotLoginLocators():
    txt_LastName = (By.ID, "forgottenFrm_lastname")
    txt_Email = (By.ID, "forgottenFrm_email")
    btnContinue = (By.CSS_SELECTOR, "#forgottenFrm>div.form-group>div>button")
    alertsuccessMessage = (By.CSS_SELECTOR, "div.alert.alert-success")
    iconCloseAlert = (By.CSS_SELECTOR, "div.alert.alert-success>button")
    alertfailedMessage =(By.CSS_SELECTOR, "div.alert.alert-error.alert-danger")
    iconCloseAlertFailed = (By.CSS_SELECTOR, " div.alert.alert-error.alert-danger>button")


class ForgotLoginPage():

    def __init__(self, driver):
        self.driver = driver

    def set_LastName(self, lastname):
        self.driver.find_element(*ForgotLoginLocators.txt_LastName).send_keys(lastname)

    def set_Email(self, email):
        self.driver.find_element(*ForgotLoginLocators.txt_Email).send_keys(email)

    def selectBtnContinue(self):
        self.driver.find_element(*ForgotLoginLocators.btnContinue).click()

    def getTextSuccesfullMessageAlert(self):
        return self.driver.find_element(*ForgotLoginLocators.alertsuccessMessage).text

    def getAlertSuccessMessage(self):
        return self.driver.find_element(*ForgotLoginLocators.alertsuccessMessage)

    def selecteIconCloseAlert(self):
        self.driver.find_element(*ForgotLoginLocators.iconCloseAlert).click()

    def getTextFailedMessageAlert(self):
        return self.driver.find_element(*ForgotLoginLocators.alertfailedMessage).text

    def getAlertFailedMessage(self):
        return self.driver.find_element(*ForgotLoginLocators.alertfailedMessage)

    def selecteIconCloseAlertFailed(self):
        self.driver.find_element(*ForgotLoginLocators.iconCloseAlertFailed).click()