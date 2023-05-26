import MySQLdb
import json


if __name__ == '__main__':
    db_connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Admin10!",
        database="personal_cars"
    )

    db_cursor = db_connection.cursor()

    db_cursor.execute("SELECT * FROM cars JOIN users ON cars.user_id = users.id;")

    cars = db_cursor.fetchall()
    for car in cars:
        print(car)

    cars = [
        {
            "id": car[0],
            "owner": {
                "id": car[5],
                "first_name": car[6],
                "last_name": car[7],
                "email": car[8],
                "address": car[9],
            },
            "brand": car[2],
            "model": car[3],
            "number": car[4]
        }
        for car in cars
    ]

    with open("raw_sql/data/all_cars_with_owner.json", "w") as file:
        json.dump(cars, file, indent=2)
