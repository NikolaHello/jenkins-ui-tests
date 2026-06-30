from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import JENKINS_URL
from pages.home_page import HomePage


class NewItemPage(HomePage):
    URL = f"{JENKINS_URL}/view/all/newJob"

    ITEM_NAME_INPUT = (By.ID, "name")
    OK_BUTTON = (By.ID, "ok-button")
    ERROR_MESSAGE = (By.ID, "itemname-required")


    # def new_item_input_displayed(self):
    #     wait = WebDriverWait(self.driver, 10)
    #     return wait.until(EC.presence_of_element_located(self.ITEM_NAME_INPUT)).is_displayed()

    def enter_item_name(self, item_name):
       self.driver.find_element(*self.ITEM_NAME_INPUT).send_keys(item_name)

    def clear_input_field(self):
        self.wait10.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='name']"))
        ).clear()

        return self

    def select_item_type(self, item_type):
        locator = (By.XPATH, f"//label[.//span[text()='{item_type}']]")
        self.driver.find_element(*locator).click()

    def ok_button_click(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(self.OK_BUTTON))
        element.click()

    def wait_configuration_page(self):
        self.wait10.until(EC.url_contains("/configure"))

    def get_error_message(self):
        return self.wait10.until(EC.presence_of_element_located(self.ERROR_MESSAGE)).text


