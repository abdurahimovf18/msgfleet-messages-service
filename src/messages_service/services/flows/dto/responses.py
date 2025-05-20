from src.messages_service.utils.dto import BaseDTO, s


class CreateUserDTO(BaseDTO):
    id: s.Message.id
    user_id: s.Message.user_id
    created_at: s.Message.created_at
    