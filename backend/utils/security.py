from passlib.hash import pbkdf2_sha256

MAX_PASSWORD_LENGTH = 72

def hash_password(password: str):
    raw = password.encode("utf-8")
    if len(raw) > MAX_PASSWORD_LENGTH:
        raise ValueError("Password must be 72 bytes or less when encoded as UTF-8.")
    return pbkdf2_sha256.hash(password)

def verify_password(password: str, hashed_password: str):
    return pbkdf2_sha256.verify(password, hashed_password)

def get_password_hash(password: str):
    return hash_password(password)
