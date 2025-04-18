from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.infrastructure.database.db_connection import get_db
from api.infrastructure.repository.user import UserRepository
from api.domain.use_case.user import AuthUseCase
from api.presentation.schema.user import UserCreate, UserLogin, UserOut, TokenOut

user_router = APIRouter()

@user_router.post("/signup", response_model=UserOut)
def signup(user_data: UserCreate, db: Session = Depends(get_db)):
    user_repo = UserRepository(db)
    auth_use_case = AuthUseCase(user_repo)
    try:
        return auth_use_case.signup(user_data.name, user_data.email, user_data.password)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@user_router.post("/login", response_model=TokenOut)
def login(login_data: UserLogin, db: Session = Depends(get_db)):
    user_repo = UserRepository(db)
    auth_use_case = AuthUseCase(user_repo)
    try:
        token = auth_use_case.login(login_data.email, login_data.password)
        return {"access_token": token, "token_type": "bearer"}
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
