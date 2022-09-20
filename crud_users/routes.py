#Python
from email.policy import default
import logging
from typing import Optional, List

# FastApi
from fastapi import APIRouter
from fastapi import Body, Depends, Query

# SQLalchemy
from sqlalchemy.orm import Session


from database.services import get_db
from .schema import *
from .model import *
from .services import *

router = APIRouter()


@router.post(
    "/auth/create",
    tags=["Users"],
    response_model = ResponseModel,
    description="Crea un registro",
)
async def create_user(user:User = Body(...), db:Session = Depends(get_db)):
    response = await create_new_user(user, db)
    return response

@router.get(
    "/auth/{id}/read",
    tags=["Users"],
    response_model = UserDB,
    description="Lee un Usuario existente a partir de su id",
)
async def read_user(id:str, db:Session = Depends(get_db)):
    """_summary_

    Args:
        id (int): _description_ Permite identificar al usuario a consultar en la base de datos
        token (str, optional): _description_.  Es la validación del nivel de acceso a la información

    Returns:
        _type_: _description_ El esquema del usuario con dichas caracteristicas consultadas
    """
    response = await read_by_id(id, db)
    return response

@router.get(
    "/auth/read",
    tags=["Users"],
    response_model = List[UserDB],
    description="Lee un Usuario existente a partir de su id",
)
async def read_users(db:Session = Depends(get_db)):
    """_summary_

    Args:
        id (int): _description_ Permite identificar al usuario a consultar en la base de datos
        token (str, optional): _description_.  Es la validación del nivel de acceso a la información

    Returns:
        _type_: _description_ El esquema del usuario con dichas caracteristicas consultadas
    """
    response = await read_all(db)
    return response


@router.put(
    "/auth/{id}/update",
    tags=["Users"],
    response_model = ResponseModel,
    description="Actualiza un Usuario existente a partir de su id",
)
async def update_user(id:str, user:User, db:Session = Depends(get_db)):
    response = await update_by_id(id, user, db)
    return response

@router.delete(
    "/auth/{id}/delete",
    tags=["Users"],
    response_model = ResponseModel,
    description="Borra un Usuario existente a partir de su id",
)
async def delete_user(id:str, db:Session = Depends(get_db)):
    response = await delete_by_id(id, db)
    return response





