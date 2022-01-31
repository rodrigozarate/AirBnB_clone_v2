#!/usr/bin/python3
""" Data Base storage using Alchemy"""

from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy import (create_engine)
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage():
    """new engine"""
    __engine = None
    __session = None

    def __init__(self):
        """ connect with db """
        host = getenv('HBNB_MYSQL_HOST')
        user = getenv('HBNB_MYSQL_USER')
        passwd = getenv('HBNB_MYSQL_PWD')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_MYSQL_ENV')
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(user, passwd, host, db),
            pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """ select all objects """
        from models.base_model import BaseModel
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        dictionary = {}

        if cls is None:
            result = self.__session.query(
                     Amenity, City, State, Place, Review, User).all()
        else:
            result = self.__session.query(cls).all()

        for obj in result:
            dictionary[obj.__class__.__name__ + '.' + obj.id] = obj

        return dictionary

    def new(self, obj):
        """add obj to session"""
        self.__session.add(obj)
        self.save()

    def save(self):
        """save changes in the session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete objects saved in the session"""
        if obj is not None:
            self.__session.delete(obj)
        self.save()

    def reload(self):
        """reload the session"""
        from models.base_model import BaseModel, Base
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """ self explanatory """
        self.__session.remove()
