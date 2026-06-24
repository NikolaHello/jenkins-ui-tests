from pages.login_page import LoginPage
from config import JENKINS_USER, JENKINS_PASSWORD
from pages.home_page import HomePage


def test_success_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(
        JENKINS_USER,
        JENKINS_PASSWORD
    )
    home_page = HomePage(driver)

    assert home_page.is_new_item_displayed()