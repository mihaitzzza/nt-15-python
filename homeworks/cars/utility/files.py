import csv
import json
import uuid
import shutil
import os
from utility.constants import OUTPUT_DIR


def clean_up_dirs():
    shutil.rmtree(OUTPUT_DIR, ignore_errors=True)
    os.makedirs(OUTPUT_DIR)


def get_input():
    data = []
    with open("input.csv") as file:
        csv_dict_reader = csv.DictReader(file)
        # for car in list(csv_dict_reader):
        # Alternative option for unique ID
        # for index, car in enumerate(csv_dict_reader):
        #     current_car = {"id": index}
        #     current_car.update(car)
        #
        #     data.append(current_car)

        for car in csv_dict_reader:
            current_car = {
                "id": str(uuid.uuid4()),
                "hp": int(car.pop("hp")),
                "price": float(car.pop("price"))
            }
            current_car.update(car)

            data.append(current_car)
    return data


def write_to_file(file_name: str, cars: list):
    with open(f"output_data/{file_name}", "w+") as file:
        json.dump(cars, file, indent=2)
