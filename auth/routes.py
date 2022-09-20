

import fastapi
from typing import List
from sqlalchemy.orm import Session
from database.services import get_db
from .schema import *
from .services import *
import logging

router = fastapi.APIRouter()


@router.post(
    "/auth/login",
    tags=["auth"],
    response_model = ResponseModel,
    description="Lee un Usuario existente a partir de su id",
)
async def login(login:Login, db:Session = fastapi.Depends(get_db)):
    response = await generate_token(login, db)
    return response





