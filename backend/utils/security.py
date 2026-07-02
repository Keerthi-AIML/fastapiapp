import bcrypt

MAX_BCRYPT_BYTES = 72

def hash_password(password: str):
    raw = password.encode("utf-8")
    if len(raw) > MAX_BCRYPT_BYTES:
        raise ValueError("Password must be 72 bytes or less when encoded as UTF-8.")
    hashed = bcrypt.hashpw(raw, bcrypt.gensalt())
    return hashed.decode("utf-8")

def verify_password(password: str, hashed_password: str):
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))

def get_password_hash(password: str):
    return hash_password(password)
