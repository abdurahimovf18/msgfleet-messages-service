from sqlalchemy.ext.asyncio import AsyncSession

from .dto import p, r
from src.messages_service.services import queries


async def create_user(param: p.CreateUserDTO, session: AsyncSession) -> r.CreateUserDTO:
    message = await queries.messages.create(
        queries.messages.p.CreateDTO(user_id=param.user_id), session)
    
    await session.commit()

    return r.CreateUserDTO.v(message)
