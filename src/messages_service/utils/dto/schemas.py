from typing import Annotated
from uuid import UUID
from datetime import datetime

from pydantic import Field

from src.messages_service.domain.models import enums
from enum import Enum


class STREnum(str, Enum):
    pass


class User:
    id = Annotated[UUID, Field()]


class Message:
    id = Annotated[UUID, Field()]
    user_id = Annotated[User.id, Field()]
    created_at = Annotated[datetime, Field()]
