import csv
from database import session, create_database_structure
from models import User, Car


def get_all_users():
    users = session.query(User).all()
    print(users)
    for user in users:
        print(user.id, user.first_name, user.last_name, user.email, user.address)
        print("he/she owns the following cars:", user.cars)
    # cars = session.query(Car).all()
    # for car in cars:
    #     print("Owner for car:", car.id, car.brand, car.model, " is ", car.user.first_name, car.user.last_name, car.user.email)


def insert_users():
    with open("raw_sql/data/input_users.csv") as file:
        csv_reader = csv.DictReader(file)
        users_data = list(csv_reader)

    print(users_data)
    for user_data in users_data:
        # user = User(first_name=user_data["first_name"], last_name=users_data["last_name"], email=user_data["email"], address=user_data["address"])
        user = User(**user_data)
        user.cars.append(Car(brand="Opel", model="Astra", plate_number="DJ01BBY"))

        session.add(user)
    session.commit()


if __name__ == '__main__':
    get_all_users()
    # insert_users()
    # create_database_structure()
