# Python
from typing import Optional
from uuid import UUID

# Pydantic
from pydantic import BaseModel
from pydantic import Field
 
        
class Login(BaseModel):
    user:str = Field(
        ..., 
        max_length=10, 
        example="Azteca2022", 
        title="Nombre del usuario", 
        description="Es el nombre del usuario compuesto por maximo 10 caracteres"
        )
    password:str = Field(
        ..., 
        min_length=8, 
        example="Pa$$w0rd", 
        title="Es la contraseña asociada al usuario", 
        description="Contraseña de minimo 8 caracteres"
        )
    
    class Config:
        orm_mode = True


class User(Login):
    level:int = Field(
        ..., 
        gt = 1, 
        le = 3, 
        title="nivel de acceso", 
        description="Es el nivel de acceso que tiene el usuario"
        )

    class Config:
        orm_mode = True


class UserDB(User):
    id:str = Field(
        ..., 
        title="Identificador", 
        description="Es la llave (id) asociada a la fila del usuario"
        )
   
    
class ResponseModel(BaseModel):
    is_success:bool = Field(
        ..., 
        title="Proceso terminado", 
        description="Describe si el proceso termino como se esperaba"
        )
    message:str = Field(
        ..., 
        title="Mensaje", 
        description="Indica el error interno de python en caso de ocurrir"
        )
