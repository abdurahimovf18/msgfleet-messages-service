from typing import Annotated
from functools import partial
from datetime import datetime
from uuid import uuid4, UUID

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey, DateTime, text
from sqlalchemy import UUID as SQLUUID

from src.messages_service.config.settings import TIMEZONE
from src.messages_service.infrastructure.db.setup import Base
from src.messages_service.domain.models import enums


id_ = Annotated[UUID, mapped_column(SQLUUID(as_uuid=True), primary_key=True, default=lambda: uuid4())]
created_at = Annotated[datetime, mapped_column(DateTime, server_default=text(f"TIMEZONE('{TIMEZONE!s}', NOW())"))]
updated_at = Annotated[datetime, mapped_column(DateTime, server_default=text(f"TIMEZONE('{TIMEZONE!s}', NOW())"), 
                                               onupdate=partial(datetime.now, TIMEZONE))]


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[id_]
    user_id: Mapped[UUID]
    created_at: Mapped[created_at]
