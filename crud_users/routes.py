

import fastapi
from typing import List
from sqlalchemy.orm import Session
from database.services import get_db
from .schema import *
from .model import *
from .services import *
import logging

router = fastapi.APIRouter()


@router.post(
    "/auth/create",
    tags=["Users"],
    response_model = ResponseModel,
    description="Crea un registro",
)
async def create_user(user:User, db:Session = fastapi.Depends(get_db), token:str = Field(default="valid")):
    response = await create_user(user, db, token)
    return response

@router.get(
    "/auth/{id}/read",
    tags=["Users"],
    response_model = ResponseModel,
    description="Lee un Usuario existente a partir de su id",
)
async def read_user(id:int, db:Session = fastapi.Depends(get_db), token:str = Field(default="valid")):
    """_summary_

    Args:
        id (int): _description_ Permite identificar al usuario a consultar en la base de datos
        token (str, optional): _description_.  Es la validación del nivel de acceso a la información

    Returns:
        _type_: _description_ El esquema del usuario con dichas caracteristicas consultadas
    """
    response = await read_by_id(id, db, token)
    return response

@router.put(
    "/auth/{id}/update",
    tags=["Users"],
    response_model = ResponseModel,
    description="Actualiza un Usuario existente a partir de su id",
)
async def update_user(id:int, user:User, db:Session = fastapi.Depends(get_db), token:str = Field(default="valid")):
    response = await update_by_id(id, user, db, token)
    return response

@router.delete(
    "/auth/{id}/delete",
    tags=["Users"],
    response_model = ResponseModel,
    description="Borra un Usuario existente a partir de su id",
)
async def delete_user(id:int, db:Session = fastapi.Depends(get_db), token:str = Field(default="valid")):
    response = await delete_by_id(id, db, token)
    return response





