from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    NEW_ITEM_LINK = (By.XPATH, "//span[text()='New Item']/..")

    def is_new_item_displayed(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.presence_of_element_located(self.NEW_ITEM_LINK)).is_displayed()

    def click_new_item(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(self.NEW_ITEM_LINK))
        element.click()



