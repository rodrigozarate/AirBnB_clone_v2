#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.sql.schema import ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from models.place import place_amenity
from os import getenv


class Amenity(BaseModel, Base):
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == 'db':

        from models.place import place_amenity
        place_amenities = relationship("Place", secondary=place_amenity,
                                       back_populates="amenities")
    else:
        place_amenities = ''
