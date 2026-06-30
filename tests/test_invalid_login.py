from pages.login_page import LoginPage



def test_login_invalid_password(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("admin", "wrong_password")

    assert "Invalid" in login_page.get_error_message()
