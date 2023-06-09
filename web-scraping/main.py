import json
import os
import shutil
from utility.browser import ChromeDriver


def prepare_directory():
    shutil.rmtree("images", ignore_errors=True)
    os.makedirs("images")


def write_output_json(raw_departments):
    departments = [department.to_dict() for department in raw_departments]

    with open("output.json", "w") as file:
        json.dump(departments, file)


if __name__ == '__main__':
    prepare_directory()

    driver = ChromeDriver()
    departments = driver.parse_departments()

    write_output_json(departments)
