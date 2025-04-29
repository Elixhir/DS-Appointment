from api.infrastructure.repository.user import UserRepository
from api.infrastructure.security import hash_password, verify_password, create_access_token

class AuthUseCase:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def signup(self, name: str, email: str, password: str):
        if self.user_repo.get_user_by_email(email):
            raise ValueError("Email ya registrado")
        hashed_pw = hash_password(password)
        return self.user_repo.create_user(name, email, hashed_pw)

    def login(self, email: str, password: str):
        user = self.user_repo.get_user_by_email(email)
        if not user or not verify_password(password, user.hashed_password):
            raise ValueError("Credenciales inválidas")
        return create_access_token(user.id, user.is_admin)

