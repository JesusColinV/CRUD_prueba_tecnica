# Python
from datetime import datetime

# Pydantic
from typing import Optional
from pydantic import BaseModel
from pydantic import Field

class Record(BaseModel):
    #id:str = Field(..., title="Identificador", description="Es la llave (id) asociada a la fila del usuario")
    nombre:str = Field(...,example = "Jesus", title = "Nombre" ,description="Nombre de la persona del registro", min_length=3, max_length=20)
    primer_apellido:str = Field(...,example = "Colin",title="Primer apellido", description="Primer apellido de la persona del registro", min_length=3, max_length=20)
    segundo_apellido:str = Field(...,example = "Vilchis", title="Segundo apellido", description="Segundo apellido de la persona del registro", min_length=3, max_length=20)
    estado_de_nacimiento:str = Field(...,example = "Estado de Mexico", title="Estado de nacimiento", description="Entidad de nacimiento de la persona del registro", min_length=3, max_length=20)
    curp:str = Field(...,title="CURP",example="COVJ980605HMCLLS03",description="Clave unica de registro de población")
    cp:int = Field(...,title="Codigo Postal",example=50180,description="Numeración regional")
    rfc:str = Field(..., title="RFC",example="COVJ980605FJ5",description="Registro federal del contribuyente")
    telefono:str = Field(...,title="telefono",example="7225664556",description="numero de comunicación telefonica", min_length=10, max_length=10)
    fecha_de_nacimiento:str = Field(...,example=datetime.now().strftime("%d-%m-%Y"),title="fecha de nacimiento", description="fecha de nacimiento en formato dd-mm-yyyy")
    
    class Config:
        orm_mode = True
        
class RecordDB(Record):
    id:str = Field(..., title="Identificador", description="Es la llave (id) asociada a la fila del usuario")

class ResponseModel(BaseModel):
    is_success:bool = Field(..., title="Proceso terminado", description="Describe si el proceso termino como se esperaba")
    message:str = Field(..., title="Mensaje", description="Indica el error interno de python en caso de ocurrir")

