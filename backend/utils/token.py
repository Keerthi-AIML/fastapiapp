from jose import jwt
from datetime import datetime, timedelta
from dotenv import load_dotenv, find_dotenv
import os
from backend.models.users import User
from fastapi import HTTPException
from sqlalchemy.orm import Session

# Load the backend .env file if present, then fall back to environment variables.
dotenv_path = find_dotenv(usecwd=True)
if not dotenv_path:
    env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
    dotenv_path = env_path if os.path.exists(env_path) else None
if dotenv_path:
    load_dotenv(dotenv_path)

SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
if not SECRET_KEY:
    SECRET_KEY = "dev-secret-key"

ALGORITHM = "HS256"

def create_access_token(data: dict, expires_delta: timedelta = timedelta(hours=2)):
    to_encode = data.copy()
    expire = datetime.now() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, key=SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_access_token(token: str, db: Session):
    try:
        to_decode = jwt.decode(token, key=SECRET_KEY, algorithms=[ALGORITHM])
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    current_user = db.query(User).filter(User.id == to_decode.get("user_id")).first()
    if current_user is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return current_user

   