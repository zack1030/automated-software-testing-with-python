import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, scoped_session

Base = declarative_base()
DB_URI = os.getenv('DB_URI', 'sqlite:///')
print('connect db {}'.format(DB_URI))

engine = create_engine(DB_URI)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

def reset_db():
    if DB_URI == 'sqlite:///':
        Base.metadata.drop_all(engine)

        from models.item import ItemModel
        Base.metadata.create_all(engine)
    else:
        raise

if __name__=='__main__':
    # e.g. env DB_URI=sqlite:///item.db python db.py
    print('drop and create {}'.format(DB_URI))
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    
