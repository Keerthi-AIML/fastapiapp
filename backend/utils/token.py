from jose import jwt
from datetime import datetime, timedelta

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(hours=2))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, key="secret", algorithm="HS256")
