from pydantic import BaseModel
import datetime
from typing import Optional

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: Optional[str] = None

class UserUpdate(BaseModel):
    
    email: Optional[str] = None
    password: Optional[str] = None
    role: Optional[str] = None
   
class UserInDBBase(UserBase):
    id_user: int 

    class Config:
        from_attributes = True  # Para mapear automáticamente a los atributos de SQLAlchemy

class User(UserInDBBase):
    pass

class UserInDB(UserInDBBase):
    pass
