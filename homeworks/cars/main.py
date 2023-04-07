from utility.files import clean_up_dirs, get_input
from utility.process import process_data

if __name__ == '__main__':
    clean_up_dirs()

    cars = get_input()

    process_data(cars)
