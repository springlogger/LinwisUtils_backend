from fastapi import Depends, HTTPException
from sqlmodel import select, Session
from app.database import get_session
from app.models import User
from app.utils.security import hash_password, verify_password

def register_user(email: str, password: str, name: str, session: Session = Depends(get_session)) -> User:
    hashed_password = hash_password(password)
    user = User(email=email, password=hashed_password, name=name)
    
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def authenticate_user(email: str, password: str, session: Session = Depends(get_session)):
    db_user = session.exec(select(User).where(User.email == email)).first()
    
    if not db_user or not verify_password(password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    return db_user