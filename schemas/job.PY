from pydantic import BaseModel
from typing import Optional

class JobCreate(BaseModel):
    name:str
    location:int

class JobUpdate(BaseModel):
    name:Optional[str]=None
    location:Optional[int]=None
