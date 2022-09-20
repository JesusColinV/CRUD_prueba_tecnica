from uuid import UUID
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import String, Integer
from database.base_class import Base

   
class Directory(Base):
    __tablename__ = 'directory'
    id = Column(String(36), primary_key=True, index = False)
    user = Column(String(16), nullable = False)
    password = Column(String(16), nullable = False)
    level = Column(Integer, nullable = False)
    
    def __str__(self):
        return self.user

