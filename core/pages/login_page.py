from core.elements.element import BasePageElement
from core.locators import *
from core.pages.basic_page import BasicPage

class LoginPage(BasicPage):

    def log_in_as(self, user):
        self.driver.find_element(LoginPageLocators.USERNAME_FIELD).send_keys(user.username)
        self.driver.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(user.password)
        self.driver.find_element(LoginPageLocators.LOG_IN_BUTTON).click()
