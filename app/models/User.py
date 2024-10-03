from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)  # Columna 'email' de tipo VARCHAR(100), única y no nula

    def __init__(self, name, email):
        """
           Constructor for the User class.

            Args:
                name (str): The name of the user
                email (str): The email address of the user
        """
        self.name = name
        self.email = email

    def __repr__(self):
        """
            String representation of a User instance, used for debugging.

            return:
                A string representing the User instance
        """
        return f"User(id={self.id} name='{self.name}' email='{self.email}')"