from sqlalchemy.orm import Session
from domain.user.user_schema import UserCreate, UserPWDUpdate
from models import User
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated='auto')

def create_user(db: Session, user_create: UserCreate):
    db_user = User(username=user_create.username,
                   password=pwd_context.hash(user_create.password1),
                   email=user_create.email)
    db.add(db_user)
    db.commit()

def get_existing_user(db: Session, user_create: UserCreate):
    return db.query(User).filter(
        (User.username == user_create.username) |
        (User.email == user_create.email)
    ).first()

def get_user(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def update_user(db: Session, user: User, update_user=UserPWDUpdate):
    user.password = pwd_context.hash(update_user.password)
    db.add(user)
    db.commit()