from pages.login_page import LoginPage


def test_login_page_title(driver):
    login_page = LoginPage(driver)
    login_page.open()
    assert "Jenkins" in login_page.get_page_title()



