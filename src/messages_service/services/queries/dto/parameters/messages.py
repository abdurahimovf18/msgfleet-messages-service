from src.messages_service.utils.dto import BaseDTO, s


class CreateDTO(BaseDTO):
    user_id: s.Message.user_id
