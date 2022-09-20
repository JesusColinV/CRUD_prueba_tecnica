from uuid import UUID
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import String, Integer, Float, Boolean, DateTime
from database.base_class import Base
   
class Record(Base):
    __tablename__ = 'record'
    id = Column(Integer, primary_key=True, index = True)
    nombre = Column(String(16), nullable = False)
    primer_apellido = Column(String(16), nullable = False)
    segundo_apellido = Column(String(16), nullable = False)
    estado_de_nacimiento = Column(String(16), nullable = False)
    curp = Column(String(16), nullable = False)
    cp = Column(String(16), nullable = False)
    rfc = Column(String(16), nullable = False)
    telefono = Column(String(16), nullable = False)
    fecha_de_nacimiento = Column(DateTime, nullable = False)

    
    