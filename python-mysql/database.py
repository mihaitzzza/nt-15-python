from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import BaseModel

connection_string = "mysql+mysqldb://{user}:{password}@{host}:{port}/{database}".format(
    user="root",
    password="Admin10!",
    host="localhost",
    port=3306,
    database="personal_cars"
)


engine = create_engine(connection_string)

SessionClass = sessionmaker(engine)
session = SessionClass()


def create_database_structure():
    BaseModel.metadata.create_all(engine)
