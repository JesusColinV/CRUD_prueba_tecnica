from uuid import UUID
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import String, Integer, Float, Boolean, Date
from database.base_class import Base
   
class Record_(Base):
    __tablename__ = 'record'
    id = Column(String(36), primary_key=True, index = False)
    nombre = Column(String(16), nullable = False)
    primer_apellido = Column(String(16), nullable = False)
    segundo_apellido = Column(String(16), nullable = False)
    estado_de_nacimiento = Column(String(16), nullable = False)
    curp = Column(String(16), nullable = False)
    cp = Column(String(16), nullable = False)
    rfc = Column(String(16), nullable = False)
    telefono = Column(String(16), nullable = False)
    fecha_de_nacimiento = Column(String(10), nullable = False)

    
    