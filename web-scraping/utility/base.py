from abc import ABC, abstractmethod


class BaseParser(ABC):
    def __init__(self, elements, driver):
        self._elements = elements[:3]
        self._driver = driver

    @abstractmethod
    def parse(self):
        raise NotImplementedError("Abstract method.")
