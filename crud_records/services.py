
from uuid import uuid1
from sqlalchemy.orm import Session
from .schema import *
from .model import Record as Model
from auth.services import auth_level

@auth_level(level = [1])
async def create_new_record(record:Record,db:Session):
    object = Model(
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
    db.add(object)
    db.commit()
    db.refresh(object)
    return ResponseModel(
        is_succes=True,
        message="Registro creado correctamente")

@auth_level(level = [1])
async def read_by_id(id:int,db:Session):
    return db.query(Model).filter(Model.id == id).fetchall()

@auth_level(level = [1,2,3])
async def read_by_id(id:int,db:Session):
    return db.query(Model).filter(Model.id == id).fetchall()

@auth_level(level = [1,2])
async def update_by_id(id:int,record:Record,db:Session):
    return db.query(Model).filter(Model.id == id).fetchall()

@auth_level(level = [1])
async def delete_by_id(id:int,db:Session):
    return db.query(Model).filter(Model.id == id).fetchall()