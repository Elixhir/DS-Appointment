from fastapi import Depends, HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from api.infrastructure.security import decode_token
from api.infrastructure.database.db_connection import get_db
from api.infrastructure.repository.user import UserRepository

bearer_scheme = HTTPBearer()

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Security(bearer_scheme),
    db=Depends(get_db),
):
    try:
        payload = decode_token(credentials.credentials)
        user_id = int(payload["sub"])
        user_repo = UserRepository(db)
        user = user_repo.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=401, detail="Usuario no encontrado")
        return user
    except:
        raise HTTPException(status_code=401, detail="Token inválido")
