from selenium.webdriver.common.by import By
from config import JENKINS_URL
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):

    URL = f"{JENKINS_URL}/login"

    USERNAME_INPUT = (By.ID, "j_username")
    PASSWORD_INPUT = (By.ID, "j_password")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Sign in']")
    ERROR_MESSAGE = (By.XPATH, "//*[contains(text(), 'Invalid')]")


    def open(self):
        self.driver.get(self.URL)

    def get_page_title(self):
        return self.driver.title

    def enter_username(self, username):
       self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        wait = WebDriverWait(self.driver, 10)

        return wait.until(EC.presence_of_element_located(self.ERROR_MESSAGE)).text
