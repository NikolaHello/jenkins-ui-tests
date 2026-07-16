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
    print("=" * 50)
    print("USER =", repr(JENKINS_USER))
    print("PASSWORD =", repr(JENKINS_PASSWORD))
    print("=" * 50)
    login_page.login(JENKINS_USER, JENKINS_PASSWORD)

    return driver