from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql
from core.config import settings
from .model_base import SqlAlchemyBase

SQALCHEMY_DATABASE_URL = settings.DATABASE_CONNECTION
engine = create_engine(SQALCHEMY_DATABASE_URL)
SqlAlchemyBase.metadata.create_all(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

