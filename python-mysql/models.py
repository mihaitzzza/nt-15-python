from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR

BaseModel = declarative_base()


class User(BaseModel):
    __tablename__ = "users"

    id = Column(INTEGER, autoincrement=True, primary_key=True)
    first_name = Column(VARCHAR(128), nullable=False)
    last_name = Column(VARCHAR(128), nullable=False)
    email = Column(VARCHAR(128), nullable=False, unique=True)
    address = Column(VARCHAR(128), nullable=True, default=None)


class Car(BaseModel):
    __tablename__ = "cars"

    id = Column(INTEGER, autoincrement=True, primary_key=True)

    user_id = Column(INTEGER, ForeignKey(User.id))
    user = relationship(User, backref="cars")

    brand = Column(VARCHAR(128), nullable=False)
    model = Column(VARCHAR(128), nullable=False)
    plate_number = Column(VARCHAR(8), nullable=False)
    type = Column((VARCHAR(10)), nullable=False, default="sedan")
