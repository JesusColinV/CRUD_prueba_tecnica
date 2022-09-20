from typing import Optional
from pydantic import BaseModel
from pydantic import Field
 
        
class Login(BaseModel):
    user:str = Field(..., max_length=10, example="Azteca2022")
    password:str = Field(..., min_length=8)
    
    class Config:
        orm_mode = True

class User(Login):
    level:int = Field(..., gt = 0, le = 4)

    class Config:
        orm_mode = True

class ResponseModel(BaseModel):
    is_succes:bool = Field(...)
    result: Optional[User]
    message:str  = Field(...)