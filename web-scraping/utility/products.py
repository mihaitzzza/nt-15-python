import requests
import uuid
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from utility.base import BaseParser


class Product:
    def __init__(self, id_, title, price, image_path):
        self.__id = id_
        self.__title = title
        self.__price = price
        self.__image_path = image_path

    def to_dict(self):
        return {
            "id": self.__id,
            "title": self.__title,
            "price": self.__price,
            "image_path": self.__image_path
        }


class ProductsParser(BaseParser):
    def parse(self):
        products = []

        for element in self._elements:
            try:
                link_element = WebDriverWait(element, 10).until(
                    element_to_be_clickable(element.find_element(By.TAG_NAME, "a"))
                )
            except Exception as e:
                print(e)
                continue

            url = link_element.get_attribute("href")

            self._driver.execute_script(f"window.open('{url}')")
            self._driver.switch_to.window(self._driver.window_handles[-1])

            # Generate unique ID
            product_id = str(uuid.uuid4())

            # Parse product data
            title_element = self._driver.find_element(By.XPATH, "//h1[@class='page-title']")
            title = title_element.text

            price_element = self._driver.find_element(
                By.XPATH,
                "//form[@class='main-product-form']//div[contains(@class, 'pricing-block')]//p[contains(@class, 'product-new-price')]"
            )
            price_with_currency = price_element.text.replace(".", "").replace(",", ".")
            price = float(price_with_currency[:-4])

            image_element = self._driver.find_element(
                By.XPATH,
                "//div[@id='product-gallery']//div[@data-ph-id='image-0']//img"
            )
            image_url = image_element.get_attribute("src")
            image_response = requests.get(image_url)
            image_path = f"images/{product_id}.jpg"
            with open(image_path, "wb") as image_file:
                image_file.write(image_response.content)

            product = Product(product_id, title, price, image_path)
            products.append(product)

            self._driver.close()
            self._driver.switch_to.window(self._driver.window_handles[-1])

        return products
