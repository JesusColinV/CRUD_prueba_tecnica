
from uuid import uuid1
from sqlalchemy.orm import Session
from .schema import *
from .model import Record_ as Model
from auth.services import auth_level

@auth_level(level = [1])
async def create_new_record(record:Record,db:Session, *args, **kwargs) -> ResponseModel:
    """_Creamos un nuevo registro_
    
    Args:
        record (Record): _Registro a almacenar_
        db (Session): _conexión a la base de datos_

    Returns:
        ResponseModel: _Respuesta_
    """
    try:
        _object = Model(
            id = str(uuid1()),
            nombre = record.nombre,
            primer_apellido = record.primer_apellido,
            segundo_apellido = record.segundo_apellido,
            estado_de_nacimiento = record.estado_de_nacimiento,
            curp = record.curp,
            cp = record.cp,
            rfc = record.rfc,
            telefono = record.telefono,
            fecha_de_nacimiento = record.fecha_de_nacimiento
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

@auth_level(level = [2])
async def read_addresses_by_id(id:str,db:Session, *args, **kwargs) -> str:
    """_A partir de un Id consultamos la dirección de un registro_
    
    Args:
        id (str): _Id del registro a consultar_
        db (Session): _Conexión a la base de datos_

    Returns:
        str: _Respuesta_
    """
    _object:Record = db.query(Model).filter(Model.id == id).first()
    return _object.estado_de_nacimiento

@auth_level(level = [1,3])
async def read_by_id(id:str,db:Session, *args, **kwargs) -> Record:
    """_A partir de un Id consultamos un registro_
    
    Args:
        id (str): _Id del registro a consultar_ 
        db (Session): _Conexión a la base de datos_ 

    Returns:
        Record: _Respuesta_
    """
    return db.query(Model).filter(Model.id == id).first()


@auth_level(level = [1,3])
async def read_all(db:Session, *args, **kwargs):
    """_Consume todos los registros_
    
    Args:
        db (Session): _Conexión a la base de datos_ 

    Returns:
        Record: _Respuesta_
    """
    return db.query(Model).all()

@auth_level(level = [1,2])
async def update_by_id(id:int,record:Record,db:Session, *args, **kwargs) -> ResponseModel:
    """_A partir de un Id actualizamos un registro_
    
    Args:
        id (int): _Id del registro a actualizar_ 
        record (Record): _Nuevo registro_ 
        db (Session): _Conexión a la base de datos_ 

    Returns:
        ResponseModel: _Respuesta_ 
    """
    try:
        _object = Model(
            id = id,
            nombre = record.nombre,
            primer_apellido = record.primer_apellido,
            segundo_apellido = record.segundo_apellido,
            estado_de_nacimiento = record.estado_de_nacimiento,
            curp = record.curp,
            cp = record.cp,
            rfc = record.rfc,
            telefono = record.telefono,
            fecha_de_nacimiento = record.fecha_de_nacimiento
        )
        db.add(_object)
        db.commit()
        db.refresh(_object)
        return ResponseModel(
            is_success=True,
            message="Registro actualizado correctamente")
    except Exception as ex:
        return ResponseModel(
            is_success=False,
            message=ex)

@auth_level(level = [1])
async def delete_by_id(id:int,db:Session, *args, **kwargs) -> ResponseModel:
    """_A partir de un Id, eliminamos el registro_
    
    Args:
        id (int): _Id del registro seleccionado_ 
        db (Session): _Conexión a la base de datos_ 

    Returns:
        ResponseModel: _Respuesta_ 
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


