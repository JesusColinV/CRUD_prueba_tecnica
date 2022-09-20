from sqlalchemy.orm import Session
from auth.services import auth_level
from sqlalchemy.orm import Session

from .schema import *
from .model import Directory as Model

@auth_level
async def create_user(user:User,db:Session):
    object = Model(
        id = 1,
        user = user.user,
        password = user.password,
        level = user.level
    )
    db.add(object)
    db.commit()
    db.refresh(object)
    return ResponseModel(
        is_succes=True,
        message="Registro creado correctamente")

@auth_level
async def read_by_id(id:int,db:Session):
    return db.query(Model).filter(Model.id == id).fetchall()

@auth_level
async def update_by_id(id:int,user:User,db:Session):
    return db.query(Model).filter(Model.id == id).fetchall()

@auth_level
async def delete_by_id(id:int,db:Session):
    return db.query(Model).filter(Model.id == id).fetchall()

