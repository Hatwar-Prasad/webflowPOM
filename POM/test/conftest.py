import pytest
from selenium import webdriver
import time

from POM.pages.HomePage import HomePage
from POM.pages.LoginPage import LoginPage


@pytest.fixture
def setup_and_teardown(request):
    driver = webdriver.Chrome()
    driver.get("https://webflow.com/made-in-webflow/plants")
    driver.maximize_window()
    driver.implicitly_wait(10)


    request.cls.homepage = HomePage(driver)
    request.cls.loginpage = LoginPage(driver)
    request.cls.driver = driver

    yield
    time.sleep(5)
    driver.quit()
