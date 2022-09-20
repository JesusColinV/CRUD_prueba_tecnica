from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from pydantic import BaseModel
from pydantic import Field

class ResponseModel(BaseModel):
    is_succes:bool = Field(..., title="Proceso terminado", description="Describe si el proceso termino como se esperaba")
    result: Optional[str] = Field(None, title="Resultado", description="Muestra el modelo resultado")
    token: Optional[str] = Field(None, title="Token", description="Es el token que permite interactuar con las apis, con los permisos apropiados")
    message:str = Field(..., title="Mensaje", description="Indica el error interno de python en caso de ocurrir")

class Login(BaseModel):
    user:str = Field(..., title="Nombre de usuario", description="Es el nombre de usuario para el inicio de sesión")
    password:str = Field(..., min_length=8, title="contraseña", description="Es la contraseña asociada al usuario")
    
    class Config:
        orm_mode = True


    