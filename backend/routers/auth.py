from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.models.users import User
from backend.schemas.token import Token
from backend.schemas.users import UserCreate, UserResponse, Login_User
from backend.utils.security import hash_password, verify_password
from backend.utils.token import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=UserResponse )
def register(user: UserCreate, db: Session = Depends(get_db)):
   
    existing_user = db.query(User).filter((User.username == user.username) | (User.email == user.email)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username or email already registered")

  
    try:
        hashed_password = hash_password(user.password)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))

   
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        role=user.role  
    )

  
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

@router.post("/login", response_model=Token)
def login(user: Login_User, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    if not verify_password(user.password, existing_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    access_token = create_access_token(data={"sub": str(existing_user.id), "role": existing_user.role})
    return {"token": access_token, "token_type": "Bearer"}
