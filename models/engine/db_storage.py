#!/usr/bin/python3
"""This module defines a class to manage Database storage for hbnb clone"""
from sqlalchemy import create_engine
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy.orm.session import sessionmaker, Session


class DBStorage:
    """This module defines a class to manage Database storage for hbnb clone"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              pool_pre_ping=True))
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session (self.__session)
        all objects depending of the class name (argument cls)"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        objects_dict = {}
        if cls is not None:
            for value in self.__session.query(cls).all():
                key = value.__class__.__name__ + '.' + value.id
                objects_dict.update({key: value})
        else:
            for key, value in classes.items():
                for object in self.__session.query(value):
                    key = object.__class__.__name__ + '.' + object.id
                    objects_dict.update({key: object})

        return(objects_dict)
