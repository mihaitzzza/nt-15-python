import os
from itertools import groupby
from utility.constants import CATEGORIES, OUTPUT_DIR
from utility.files import write_to_file


def process_data(cars: list):
    for key, condition_function in CATEGORIES.items():
        data = [car for car in cars if condition_function(car)]
        write_to_file(f"{key}.json", data)

    # brands = set(car["brand"].lower() for car in cars)
    # os.makedirs(f"{OUTPUT_DIR}/brands")
    #
    # for brand in brands:
    #     data = [car for car in cars if car["brand"].lower() == brand]
    #     write_to_file(f"brands/{brand}.json", data)

    os.makedirs(f"{OUTPUT_DIR}/brands")
    for brand, group in groupby(cars, key=lambda car: car["brand"]):
        write_to_file(f"brands/{brand.lower()}.json", list(group))
