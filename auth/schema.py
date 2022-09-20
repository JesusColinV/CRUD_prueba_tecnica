from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from pydantic import BaseModel
from pydantic import Field

class ResponseModel(BaseModel):
    is_succes:bool = Field(...)
    result: Optional[str] = Field()
    message:str = Field(...)

class Login(BaseModel):
    user:str = Field(...)
    password:str = Field(..., min_length=8)
    
    class Config:
        orm_mode = True


    