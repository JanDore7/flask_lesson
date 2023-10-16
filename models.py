from atexit import register
from sqlalchemy import create_engine, Column, String, DateTime, func, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


PG_USER = 'app'
PG_PASSWORD = '1234'
PG_DB = 'app'
PG_HOST = '127.0.0.1'
PG_PORT = 5431

PG_DSN = f'postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}'
engin = create_engine(PG_DSN)
register(engin.dispose)
Session = sessionmaker(bind=engin)
Base = declarative_base(bind=engin)


class User(Base):

    __tablename__ = 'app_users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    creation_time = Column(DateTime, server_default=func.now())


Base.metadata.create_all()