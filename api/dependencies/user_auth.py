from fastapi import Depends, HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from api.infrastructure.security import decode_token
bearer_scheme = HTTPBearer()
from pydantic import BaseModel

class TokenUser(BaseModel):
    id: int
    is_admin: bool

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Security(bearer_scheme),
):
    try:
        payload = decode_token(credentials.credentials)
        user = TokenUser(
            id=int(payload["sub"]),
            is_admin=payload["is_admin"]
        )
        return user
    except:
        raise HTTPException(status_code=401, detail="Token inválido")

def get_admin_user(current_user: TokenUser = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Acceso restringido solo para administradores")
    return current_user

