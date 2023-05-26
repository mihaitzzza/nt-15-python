import MySQLdb
import csv


def get_users_from_file():
    with open("data/input_users.csv") as file:
        csv_reader = csv.DictReader(file)
        return list(csv_reader)


if __name__ == '__main__':
    db_connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Admin10!",
        database="personal_cars"
    )

    db_cursor = db_connection.cursor()

    users = get_users_from_file()
    print(users)

    db_cursor.executemany("INSERT INTO users(first_name, last_name, email, address) VALUES(%s, %s, %s, %s);", (
        (user["first_name"], user["last_name"], user["email"], user["address"])
        for user in users
    ))

    db_connection.commit()
