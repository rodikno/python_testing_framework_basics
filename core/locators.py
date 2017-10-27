from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    USERNAME_FIELD = (By.ID, 'username')
    PASSWORD_FIELD = (By.ID, 'password')
    LOG_IN_BUTTON = (By.NAME, 'login')


class RegistrationPageLocators(object):
    pass


class MainPageLocators(object):
    pass