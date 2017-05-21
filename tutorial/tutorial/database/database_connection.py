from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
import os

Base = declarative_base()
Engine = create_engine('sqlite:///:memory:', echo=True)
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))

engine = create_engine('sqlite:///' + CURRENT_PATH + '/data.db', echo=True)


class FootballItemDataBase(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    copo = Column(String)
    date = Column(String)


class DataBase_Service:
    def __init__(self):
        self.session = scoped_session(sessionmaker(bind=engine))

    def add_football_item(self, item):
        self.session.add(item)
        self.session.commit()


Base.metadata.create_all(engine)

