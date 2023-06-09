from selenium.webdriver.common.by import By
from utility.base import BaseParser
from utility.categories import CategoriesParser


class Department:
    def __init__(self, name, categories):
        self.__name = name
        self.__categories = categories

    def to_dict(self):
        return {
            "name": self.__name,
            "categories": [category.to_dict() for category in self.__categories]
        }


class DepartmentsParser(BaseParser):
    def parse(self):
        departments = []

        for element in self._elements:
            header_element = element.find_element(By.TAG_NAME, "h3")

            category_elements = element.find_elements(By.XPATH, ".//div[contains(@class, 'subdepartment-col')]")
            categories_parser = CategoriesParser(category_elements, self._driver)
            categories = categories_parser.parse()

            department = Department(header_element.text, categories)
            departments.append(department)

        return departments
