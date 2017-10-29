import time
import pytest
from selenium import webdriver
from core.pages.login_page import LoginPage
from core.pages.basic_page import BasicPage
from core.helper_classes.user import *

class TestLogIn(object):
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.user = ValidUser()
        cls.user_with_incorrect_pass = UserWithIncorrectPassword()
        cls.page = BasicPage(cls.driver)

    @classmethod
    def teardown_class(cls):
        cls.driver.close()


    def teardown_method(self):
        self.page.log_out()


    def test_log_in_positive(self):
        login_page = LoginPage(self.driver)
        login_page.open_page()
        login_page.log_in_as(self.user)


    def test_log_in_incorrect_password(self):
        login_page = LoginPage(self.driver)
        login_page.open_page()
        login_page.log_in_as(self.user)