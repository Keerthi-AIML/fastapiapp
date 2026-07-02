from pydantic import BaseModel, constr

class UserBase(BaseModel):
    username: str
    email: str
    role: str

class UserCreate(UserBase):
    password: constr(max_length=72)

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True