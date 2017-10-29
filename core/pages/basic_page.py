from core.locators import BasicPageLocators


class BasicPage(object):
    PAGE_URL = None

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        if self.PAGE_URL:
            self.driver.get(self.PAGE_URL)
        else:
            raise BaseException(f'RAISED: PAGE_URL is not set for current {type(self)} instance')

    def log_out(self):
        self.driver.find_element(*BasicPageLocators.LOG_OUT_BUTTON).click()
