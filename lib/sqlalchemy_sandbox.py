#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# defining the Student class with SQLAlchemy
class Student(Base):
     __tablename__ = 'students'
# creating columns (2 of them)
     id = Column(Integer(), primary_key=True)
     name = Column(String())
# Setting up the create_engine and call create_all() to create the students table in a database (students.db).
if __name__ == '__main__':
     engine = create_engine('sqlite:///students.db')
     Base.metadata.create_all(engine)
   