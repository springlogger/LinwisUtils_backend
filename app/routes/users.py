from fastapi import APIRouter, Depends
from app.models import User
from app.auth import register_user, authenticate_user
from app.database import get_session
from sqlmodel import Session

router = APIRouter()

@router.post("/register/")
def create_user(user: User, session: Session = Depends(get_session)):
    print(user)
    return register_user(user.email, user.password, user.name, session)

@router.post("/login/")
def login_user(email: str, password: str, session: Session = Depends(get_session)):
    return authenticate_user(email, password, session)