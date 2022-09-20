from uuid import UUID
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import String, Integer, Float, Boolean
from database.base_class import Base

   
class Directory(Base):
    __tablename__ = 'directory'
    id = Column(Integer, primary_key=True, index = True)
    user = Column(String(16), nullable = False)
    pasword = Column(Float)
    level = Column(Integer, nullable = False)

