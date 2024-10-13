from selenium.webdriver.common.by import By

from POM.pages.BaseClass import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver
        self.email_field=(By.ID,"email-input")
        self.password_field=(By.ID,"password-input")
        self.login_Btn=(By.XPATH,"//span[text()='Log in']")

    def login(self,username,password):
        self.sendkeys(self.email_field,username)
        self.sendkeys(self.password_field,password)
        self.click(self.login_Btn)
