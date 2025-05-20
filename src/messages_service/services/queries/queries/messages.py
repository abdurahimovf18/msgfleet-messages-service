from sqlalchemy.ext.asyncio import AsyncSession
import sqlalchemy as sa
from sqlalchemy.orm import load_only

from src.messages_service.infrastructure.db import models

from ..dto.parameters import messages as p
from ..dto.responses import messages as r



async def create(param: p.CreateDTO, session: AsyncSession) -> r.CreateDTO:
    message = models.Message(user_id=param.user_id)
    session.add(message)
    await session.flush([message])
    return r.CreateDTO.model_validate(message)
