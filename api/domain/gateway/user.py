from abc import ABC, abstractmethod
from api.domain.entity.user import User

class UserGateway(ABC):
    @abstractmethod
    def get_user_by_email(self, email: str) -> User | None:
        pass

    @abstractmethod
    def create_user(self, name: str, email: str, hashed_password: str) -> User:
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> User | None:
        pass
