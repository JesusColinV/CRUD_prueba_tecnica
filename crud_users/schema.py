# Python
from typing import Optional
from uuid import UUID

# Pydantic
from pydantic import BaseModel
from pydantic import Field
 
        
class Login(BaseModel):
    user:str = Field(..., max_length=10, example="Azteca2022")
    password:str = Field(..., min_length=8, example="Pa$$w0rd")
    
    class Config:
        orm_mode = True

class User(Login):
    level:int = Field(..., gt = 1, le = 3)

    class Config:
        orm_mode = True


class UserDB(User):
    id:str
class ResponseModel(BaseModel):
    is_success:bool = Field(...)
    result: Optional[User] = None
    message:str  = Field(...)