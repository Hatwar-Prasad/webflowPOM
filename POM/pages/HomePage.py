from selenium.webdriver.common.by import By

from POM.pages.BaseClass import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.login_btn=(By.XPATH,"//span[text()='Login']")

    def signIn_btn(self):
        self.click(self.login_btn)