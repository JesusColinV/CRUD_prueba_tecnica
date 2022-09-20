from sqlalchemy.orm import Session
from uuid import uuid1

from .schema import *
from .model import Directory as Model


async def create_new_user(user:User, db:Session) -> ResponseModel:
    """_summary_
    Agregamos un usuario a la base de datos
    
    Args:
        user (User): _Datos del usuario a registrarse_  
        db (Session): _Conexión a la base de datos_ 

    Returns:
        ResponseModel: _Respuesta _ 
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
            is_success = True,
            message = "Registro creado correctamente")
    except Exception as ex:
        return ResponseModel(
            is_success = False,
            message = ex)


async def read_by_id(id:int, db:Session):
    """_summary_
    Consultamos los datos de un usuario a partir de su id
    Args:
        id (int): _Id del usuario a leer_ 
        db (Session): _Conexión a la base de datos_ 

    Returns:
        User (User)
    """
    return db.query(Model).filter(Model.id == id).first()


async def read_all(db:Session):
    """_summary_
    Consultamos los datos de todos los usuarios
    Args:
        db (Session): _Conexión a la base de datos_ 

    Returns:
        Users (List)
    """
    return db.query(Model).all()


async def update_by_id(id:str, user:User, db:Session) -> ResponseModel:
    """_summary_
    Actualizamos los datos de un usuario a partir de su id
    Args:
        id (int): _Id del usuario a actualizar_ 
        user (User): _Datos del usuario a actualizar _ 
        db (Session): _Conexión a la base de datos_ 

    Returns:
        ResponseModel: _Respuesta_  
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
            is_success = True,
            message = "Registro creado correctamente")
    except Exception as ex:
        return ResponseModel(
            is_success = False,
            message = ex)


async def delete_by_id(id:int, db:Session) -> ResponseModel:
    """_summary_
    Borramos un usuario a partir de un id
    Args:
        id (int): _Id del usuario a borrar_ 
        db (Session): _Conexión a la base de datos_ 

    Returns:
        ResponseModel: _Respuesta_  
    """
    try:
        db.query(Model).filter(Model.id == id).delete()
        db.commit()
        return ResponseModel(
            is_success = True,
            message = "Registro eliminado")
    except Exception as ex:
        return ResponseModel(
            is_success = False,
            message = ex)




