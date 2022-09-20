from datetime import datetime
from pydantic import BaseModel
#from PIL import Image
from pydantic import Field


class Record(BaseModel):
    id:int = Field(...)
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
    result:str = Field(...)
    message:str = Field(...)

