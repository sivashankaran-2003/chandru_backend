from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str # 'admin' or 'user'

class UserOut(BaseModel):
    name: str
    email: EmailStr
    role: str
