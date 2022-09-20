# Python
from datetime import datetime

# Pydantic
from typing import Optional
from pydantic import BaseModel
from pydantic import Field

class Record(BaseModel):
    id:str = Field(...)
    nombre:str = Field(...)
    primer_apellido:str = Field(...)
    segundo_apellido:str = Field(...)
    estado_de_nacimiento:str = Field(...)
    curp:str = Field(...)
    cp:int = Field(...)
    rfc:str = Field(...)
    telefono:str = Field(...)
    fecha_de_nacimiento:datetime = Field(...)
    
    class Config:
        orm_mode = True
        

class ResponseModel(BaseModel):
    is_succes:bool = Field(...)
    result: Optional[str] = None
    message:str = Field(...)

