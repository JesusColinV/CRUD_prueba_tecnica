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
    "/crud/{id}/create",
    tags=["CRUD"],
    response_model = ResponseModel,
    description="Crea un registro",
)
async def create_record(record:Record, db:Session = fastapi.Depends(get_db), token:str = Field(default="valid")):
    response = await create_record(record, db, token)
    return response

@router.get(
    "/crud/{id}/read",
    tags=["CRUD"],
    response_model = ResponseModel,
    description="Lee un registro existente a partir de su id",
)
async def read_record(id:int, db:Session = fastapi.Depends(get_db), token:str = Field(default="valid")):
    response = await read_by_id(id, db, token)
    return response

@router.put(
    "/crud/{id}/update",
    tags=["CRUD"],
    response_model = ResponseModel,
    description="Actualiza un registro existente a partir de su id",
)
async def update_record(id:int, record:Record, db:Session = fastapi.Depends(get_db), token:str = Field(default="valid")):
    response = await update_by_id(id, record, db, token)
    return response

@router.delete(
    "/crud/{id}/delete",
    tags=["CRUD"],
    response_model = ResponseModel,
    description="Borra un registro existente a partir de su id",
)
async def delete_record(id:int, db:Session = fastapi.Depends(get_db), token:str = Field(default="valid")):
    response = await delete_by_id(id, db, token)
    return response