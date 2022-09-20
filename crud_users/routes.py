#Python
from email.policy import default
import logging
from typing import Optional, List

# FastApi
from fastapi import APIRouter
from fastapi import Body, Depends, Path
from fastapi import status

# SQLalchemy
from sqlalchemy.orm import Session

# Development
from database.services import get_db
from .schema import *
from .model import *
from .services import *


router = APIRouter()


@router.post(
    "/auth/create",
    tags = ["Users"],
    response_model = ResponseModel,
    status_code = status.HTTP_201_CREATED,
    description = "Crea un registro",
)
async def create_user(user:User = Body(...), db:Session = Depends(get_db)):
    """_creación de un usuario_

    Args:
        user (User, optional): _Información del usuario a crear_. Defaults to Body(...).
        db (Session, optional): _Conexión a base de datos_. Defaults to Depends(get_db).

    Returns:
        _response_: _resultado del procedimiento_
    """
    response = await create_new_user(user, db)
    return response


@router.get(
    "/auth/{id}/read",
    tags = ["Users"],
    response_model = UserDB,
    status_code = status.HTTP_200_OK,
    description = "Lee un Usuario existente a partir de su id",
)
async def read_user(id:str = Path(...), db:Session = Depends(get_db)):
    """_lectura de un usuario a partir de id_

    Args:
        id (int): _Permite identificar al usuario a consultar en la base de datos_ 
        token (str, optional): _Es la validación del nivel de acceso a la información_  

    Returns:
        _response_: _El esquema del usuario con dichas caracteristicas consultadas_ 
    """
    response = await read_by_id(id, db)
    return response


@router.get(
    "/auth/read",
    tags = ["Users"],
    response_model = List[UserDB],
    status_code = status.HTTP_200_OK,
    description = "Lee un Usuario existente a partir de su id",
)
async def read_users(db:Session = Depends(get_db)):
    """_Lectura de usuarios disponibles_

    Args:
        id (int): _Permite identificar al usuario a consultar en la base de datos_ 
        token (str, optional): _dEs la validación del nivel de acceso a la información_

    Returns:
        _response_: _El esquema del usuario con dichas caracteristicas consultadas_ 
    """
    response = await read_all(db)
    return response


@router.put(
    "/auth/{id}/update",
    tags = ["Users"],
    response_model = ResponseModel,
    status_code = status.HTTP_200_OK,
    description = "Actualiza un Usuario existente a partir de su id",
)
async def update_user(id:str = Path(...), user:User = Body(...), 
                      db:Session = Depends(get_db)):
    response = await update_by_id(id, user, db)
    return response

@router.delete(
    "/auth/{id}/delete",
    tags = ["Users"],
    response_model = ResponseModel,
    status_code = status.HTTP_200_OK,
    description = "Borra un Usuario existente a partir de su id",
)
async def delete_user(id:str = Path(...), db:Session = Depends(get_db)):
    """_Borrar a un usuario a partir de su id_

    Args:
        id (str, optional): _id del usuario a borrar_. Defaults to Path(...).
        db (Session, optional): _Conexión a la base de datos_. Defaults to Depends(get_db).

    Returns:
        _response_: _resultado del procedimiento_
    """
    response = await delete_by_id(id, db)
    return response





