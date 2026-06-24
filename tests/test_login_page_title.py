from pages.login_page import LoginPage
from config import JENKINS_USER, JENKINS_PASSWORD


def test_login_page_title(driver):
    login_page = LoginPage(driver)
    login_page.open()
    assert "Jenkins" in login_page.get_page_title()

def test_success_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(
        JENKINS_USER,
        JENKINS_PASSWORD
    )
    assert 

