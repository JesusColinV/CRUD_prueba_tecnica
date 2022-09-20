from sqlalchemy.orm import Session
from auth.services import auth_level
from sqlalchemy.orm import Session
from uuid import uuid1

from .schema import *
from .model import Directory as Model


async def create_new_user(user:User,db:Session) -> ResponseModel:
    """_summary_
    Agregamos un usuario a la base de datos
    
    Args:
        user (User): _description_ Datos del usuario a registrarse 
        db (Session): _description_ Conexión a la base de datos

    Returns:
        ResponseModel: _description_ Respuesta 
    """
    try:
        _object = Model(
            id = str(uuid1()),
            user = user.user,
            password = user.password,
            level = user.level
        )
        db.add(_object)
        db.commit()
        db.refresh(_object)
        return ResponseModel(
            is_success=True,
            message="Registro creado correctamente")
    except Exception as ex:
        return ResponseModel(
            is_success=False,
            message=ex)


async def read_by_id(id:int,db:Session):
    """_summary_
    Consultamos los datos de un usuario a partir de su id
    Args:
        id (int): _description_ Id del usuario a leer
        db (Session): _description_ Conexión a la base de datos

    Returns:
        User (User)
    """
    return db.query(Model).filter(Model.id == id).first()


async def read_all(db:Session):
    """_summary_
    Consultamos los datos de todos los usuarios
    Args:
        db (Session): _description_ Conexión a la base de datos

    Returns:
        Users (List)
    """
    return db.query(Model).all()


async def update_by_id(id:str,user:User,db:Session) -> ResponseModel:
    """_summary_
    Actualizamos los datos de un usuario a partir de su id
    Args:
        id (int): _description_ Id del usuario a actualizar
        user (User): _description_ Datos del usuario a actualizar 
        db (Session): _description_ Conexión a la base de datos

    Returns:
        ResponseModel: _description_ Respuesta 
    """
    try:
        _object = Model(
            id = id,
            user = user.user,
            password = user.password,
            level = user.level
        )
        db.add(_object)
        db.commit()
        db.refresh(_object)
        return ResponseModel(
            is_success=True,
            message="Registro creado correctamente")
    except Exception as ex:
        return ResponseModel(
            is_success=False,
            message=ex)


async def delete_by_id(id:int,db:Session) -> ResponseModel:
    """_summary_
    Borramos un usuario a partir de un id
    Args:
        id (int): _description_ Id del usuario a borrar
        db (Session): _description_ Conexión a la base de datos

    Returns:
        ResponseModel: _description_ Respuesta 
    """
    try:
        db.query(Model).filter(Model.id == id).delete()
        db.commit()
        return ResponseModel(
            is_success=True,
            message="Registro eliminado")
    except Exception as ex:
        return ResponseModel(
            is_success=False,
            message=ex)




