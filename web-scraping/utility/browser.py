from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from utility.departments import DepartmentsParser


class ChromeDriver:
    def __init__(self):
        service = Service(executable_path="./chromedriver")

        self.__driver = Chrome(service=service)
        self.__driver.set_window_position(0, 0)
        self.__driver.maximize_window()

        self.__driver.get("https://www.emag.ro/all-departments")

    def parse_departments(self):
        elements = self.__driver.find_elements(By.XPATH, "//div[contains(@class, 'department-panel')]")

        departments_parser = DepartmentsParser(elements, self.__driver)
        departments = departments_parser.parse()

        return departments
