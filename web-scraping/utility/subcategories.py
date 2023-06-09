from selenium.webdriver.common.by import By
from utility.base import BaseParser
from utility.products import ProductsParser


class Subcategory:
    def __init__(self, name, products):
        self.__name = name
        self.__products = products

    def to_dict(self):
        return {
            "name": self.__name,
            "products": [product.to_dict() for product in self.__products]
        }


class SubcategoriesParser(BaseParser):
    def parse(self):
        subcategories = []

        for element in self._elements:
            link_element = element.find_element(By.TAG_NAME, "a")
            subcategory_name = link_element.text
            url = link_element.get_attribute("href")
            print('link_element', )

            self._driver.execute_script(f"window.open('{url}')")
            self._driver.switch_to.window(self._driver.window_handles[-1])

            # Identify products container (container with all products inside)
            container = self._driver.find_element(By.XPATH, "//div[@id='card_grid']")

            # Identify product elements (container of a product details)
            product_elements = container.find_elements(By.XPATH, ".//div[contains(@class, 'card-item')]")
            products_parser = ProductsParser(product_elements, self._driver)
            products = products_parser.parse()
            print('products', products)

            subcategory = Subcategory(subcategory_name, products)
            subcategories.append(subcategory)

            self._driver.close()
            self._driver.switch_to.window(self._driver.window_handles[-1])

        return subcategories
