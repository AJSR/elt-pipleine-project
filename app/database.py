from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

READER_SQLALCHEMY_DATABASE_URL= f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}'
GOD_SQLALCHEMY_DATABASE_URL= f'postgresql://{settings.database_god}:{settings.database_god_password}@{settings.database_hostname}/{settings.database_name}'

reader_engine = create_engine(READER_SQLALCHEMY_DATABASE_URL)
god_engine = create_engine(GOD_SQLALCHEMY_DATABASE_URL)

SessionLocalReader = sessionmaker(autocommit=False, autoflush=False, bind=reader_engine)
SessionLocalGod = sessionmaker(autocommit=False, autoflush=False, bind=god_engine)

Base = declarative_base()

def get_reader_db():
    db = SessionLocalReader()
    try:
        yield db
    finally:
        db.close()

def get_god_db():
    db = SessionLocalGod()
    try:
        yield db
    finally:
        db.close()
