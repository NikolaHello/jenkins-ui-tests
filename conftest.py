import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from config import JENKINS_USER, JENKINS_PASSWORD


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def logged_in(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(JENKINS_USER, JENKINS_PASSWORD)

    return driver