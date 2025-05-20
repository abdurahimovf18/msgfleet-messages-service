from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from src.messages_service.domain.models import enums


@dataclass
class Messages:
    id: UUID
    user_id: UUID
    created_at: datetime
    
