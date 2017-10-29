from core.elements.element import BasePageElement
from core.locators import LoginPageLocators
from core.pages.basic_page import BasicPage

class LoginPage(BasicPage):

    PAGE_URL = 'http://demo.redmine.org/login'

    def log_in_as(self, user):
        self.driver.find_element(*LoginPageLocators.USERNAME_FIELD).send_keys(user.username)
        self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(user.password)
        self.driver.find_element(*LoginPageLocators.LOG_IN_BUTTON).click()
