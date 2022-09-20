#Python
import logging
from typing import List, Optional

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
    "/crud/{id}/create",
    tags=["CRUD"],
    response_model = ResponseModel,
    description="Crea un registro",
)
async def create_record(record:Record = Body(...), db:Session = Depends(get_db), 
                        token:Optional[str] = Query(default="valid")):
    response = await create_new_record(record, db, token)
    return response

@router.get(
    "/crud/{id}/read",
    tags=["CRUD"],
    response_model = ResponseModel,
    description="Lee un registro existente a partir de su id",
)
async def read_record(id:str, db:Session = Depends(get_db), 
                      token:Optional[str] = Query(default="valid")):
    response = await read_by_id(id, db, token)
    return response

@router.put(
    "/crud/{id}/update",
    tags=["CRUD"],
    response_model = ResponseModel,
    description="Actualiza un registro existente a partir de su id",
)
async def update_record(id:str, record:Record, db:Session = Depends(get_db), 
                        token:Optional[str] = Query(default="valid")):
    response = await update_by_id(id, record, db, token)
    return response

@router.delete(
    "/crud/{id}/delete",
    tags=["CRUD"],
    response_model = ResponseModel,
    description="Borra un registro existente a partir de su id",
)
async def delete_record(id:str, db:Session = Depends(get_db), 
                        token:Optional[str] = Query(default="valid")):
    response = await delete_by_id(id, db, token)
    return response