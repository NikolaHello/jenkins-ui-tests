import uuid
from conftest import driver
from pages.home_page import HomePage
from pages.login_page import LoginPage
from config import JENKINS_USER, JENKINS_PASSWORD
from pages.new_item_page import NewItemPage


item_name = f"test_project_{uuid.uuid4().hex[:8]}"
invalid_character = f"{item_name}_['?', '*', '/', '!', '%', '$', '&', ';', ':', '@', '>']"
item_type = ["Pipeline", "Freestyle project", "Multi-configuration project", "Folder", "Multibranch Pipeline",
           "Organization Folder"]



"""класс позитивных тестов 
- открывается страница нью айтем
- вводим корретное название
- выбираем тип
- нажимаем кнопку ок
"""

"""класс негативных тестов 
1. некорректное имя
- открывается страница нью айтем
- вводим корретное название

2. без выбора item type кнопка ок задизейблена
"""


class TestNewItem:
    def test_open_new_item_page(self, logged_in):
        home_page = HomePage(logged_in)
        home_page.click_new_item()
        new_item_page = NewItemPage(logged_in)
        new_item_page.enter_item_name(item_name)
        new_item_page.select_item_type("Pipeline")
        new_item_page.ok_button_click()
        new_item_page.wait_configuration_page()

        assert "/configure" in logged_in.current_url

    def test_create_project(self, driver):
        pass



class NewItemNegative:
    def test_invalid_name(self, driver):
        pass


    def test_empty_name(self, driver):
        pass