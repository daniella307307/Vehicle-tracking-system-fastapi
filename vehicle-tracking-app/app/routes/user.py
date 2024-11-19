import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from bcrypt import hashpw, gensalt
from uuid import uuid4

from database import get_db,Base
from app.models.user import CustomUser, Profile

from schemas import UserCreate, UserRead, ProfileRead

router = APIRouter()


@router.post("/users/create", response_model=UserRead, status_code=201)
async def create_user(user: UserCreate,db:Session = Depends(get_db)):
    existing_user = db.query(CustomUser).filter(CustomUser.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    hashed_password = hashpw(user.password.encode('utf-8'), gensalt())
    db_user = CustomUser( 
        username=user.username,
        email=user.email,
        password=hashed_password,
        role=user.role,
    )
    db.add(db_user)
    db.commit()
    
    return {
        "id": db_user.id,
        "username": db_user.username,
        "email": db_user.email,
        "role": db_user.role,
    }


@router.get("/users/{user_id}", response_model=UserRead)
def get_user(user_id: str, db: Session = Depends(get_db)):

    user = db.query(CustomUser).filter(CustomUser.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/users/", response_model=list[UserRead])
def list_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
   
    users = db.query(CustomUser).offset(skip).limit(limit).all()
    return users


@router.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: str, db: Session = Depends(get_db)):
   
    user = db.query(CustomUser).filter(CustomUser.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}


@router.get("/users/{user_id}", response_model=UserRead)
def get_user(user_id: str, db: Session = Depends(get_db)):
   
    user = db.query(CustomUser).filter(CustomUser.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Profile not found")
    return {"Message": "User deleted successfully"}
