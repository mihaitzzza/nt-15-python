from selenium.webdriver.common.by import By
from utility.base import BaseParser
from utility.subcategories import SubcategoriesParser


class Category:
    def __init__(self, name, categories):
        self.__name = name
        self.__categories = categories

    def to_dict(self):
        return {
            "name": self.__name,
            "categories": [category.to_dict() for category in self.__categories]
        }


class CategoriesParser(BaseParser):
    def parse(self):
        categories = []

        for element in self._elements:
            header_element = element.find_element(By.TAG_NAME, "h4")

            subcategory_elements = element.find_elements(By.XPATH, ".//ul/li")
            subcategories_parser = SubcategoriesParser(subcategory_elements, self._driver)
            subcategories = subcategories_parser.parse()
            print('subcategories', subcategories)

            category = Category(header_element.text, subcategories)
            categories.append(category)

        return categories
