from fastapi import APIRouter, Depends, Body

from src.messages_service.services import flows
from .dto import p, r

from src.messages_service.services.dependencies import db


router = APIRouter()


@router.post("/create")
async def create(
    param: p.CreateDTO = Body(...),
    session = Depends(db.session)) -> r.CreateDTO:
    
    created_user = await flows.create_user(
        flows.p.CreateUserDTO(user_id=param.user_id), session)
    
    return r.CreateDTO.v(created_user)
