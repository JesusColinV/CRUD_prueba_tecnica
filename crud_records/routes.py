#Python
import logging
from typing import List, Optional

# FastApi
from fastapi import APIRouter
from fastapi import Body, Depends, Query, Path
from fastapi import status
from fastapi import HTTPException

# SQLalchemy
from sqlalchemy.orm import Session


from database.services import get_db
from .schema import *
from .model import *
from .services import *
from validator.service import Validator


router = APIRouter()


@router.post(
    "/crud/create",
    tags = ["CRUD"],
    response_model = ResponseModel,
    status_code = status.HTTP_201_CREATED,
    description = "Crea un registro",
)
async def create_record(record:Record = Body(...), db:Session = Depends(get_db), 
                        token:Optional[str] = Query(
                            default="lvl1",
                            title="validated token",
                            description="Es un token que identifica que se haya iniciado sesión y los permisos para el uso de las funciones"
                            )):
    
    
    try:
        Validator(record)
        response = await create_new_record(record, db, token)
        return response
    
    
    except NotADirectoryError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED
        )
        
        
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(ex)
        )

@router.get(
    "/crud/{id}/read",
    tags = ["CRUD"],
    response_model = RecordDB,
    status_code = status.HTTP_200_OK,
    description = "Lee un registro existente a partir de su id",
)
async def read_record(id:str = Path(...), db:Session = Depends(get_db), 
                      token:Optional[str] = Query(
                            default="lvl1",
                            title="validated token",
                            description="Es un token que identifica que se haya iniciado sesión y los permisos para el uso de las funciones"
                            )):
    try:
        response = await read_by_id(id, db, token)
        return response
    
    
    except NotADirectoryError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED
        )
        
        
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(ex)
        )
        
@router.get(
    "/crud/{id}/read/addresses",
    tags=["CRUD"],
    status_code=status.HTTP_200_OK,
    description="Lee un registro existente a partir de su id",
)
async def read_record_addresses(id:str = Path(...), db:Session = Depends(get_db), 
                      token:Optional[str] = Query(
                            default="lvl1",
                            title="validated token",
                            description="Es un token que identifica que se haya iniciado sesión y los permisos para el uso de las funciones"
                            )):
    try:
        response = await read_addresses_by_id(id, db, token)
        return {"addresses":response}
    
    
    except NotADirectoryError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED
        )
        
        
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail = str(ex)
        )
        
@router.get(
    "/crud/read",
    tags = ["CRUD"],
    response_model = List[RecordDB],
    status_code = status.HTTP_200_OK,
    description = "Lee todos los registros existentes",
)
async def read_records(db:Session = Depends(get_db), 
                      token:Optional[str] = Query(
                            default = "lvl1",
                            title = "validated token",
                            description = "Es un token que identifica que se haya iniciado sesión y los permisos para el uso de las funciones"
                            )):
    try:
        response = await read_all(db, token)
        return response
    
    
    except NotADirectoryError:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED
        )
        
        
    except Exception as ex:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = str(ex)
        )      
        
        

@router.put(
    "/crud/{id}/update",
    tags = ["CRUD"],
    response_model = ResponseModel,
    description="Actualiza un registro existente a partir de su id",
)
async def update_record(id:str = Path(...), record:Record = Body(...), db:Session = Depends(get_db), 
                        token:Optional[str] = Query(
                            default = "lvl1",
                            title = "validated token",
                            description = "Es un token que identifica que se haya iniciado sesión y los permisos para el uso de las funciones"
                            )):
    try:
        response = await update_by_id(id, record, db, token)
        return response
    
    
    except NotADirectoryError:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED
        )
        
        
    except Exception as ex:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = str(ex)
        )

@router.delete(
    "/crud/{id}/delete",
    tags = ["CRUD"],
    response_model = ResponseModel,
    description = "Borra un registro existente a partir de su id",
)
async def delete_record(id:str = Path(...), db:Session = Depends(get_db), 
                        token:Optional[str] = Query(
                            default = "lvl1",
                            title = "validated token",
                            description = "Es un token que identifica que se haya iniciado sesión y los permisos para el uso de las funciones"
                            )):
    try:
        response = await delete_by_id(id, db, token)
        return response
    
    
    except NotADirectoryError:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED
        )
        
        
    except Exception as ex:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = str(ex)
        )