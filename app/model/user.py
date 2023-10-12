from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str
    role: str
    name: str
    email: str

class UserUpdate(BaseModel):
    username: str
    role: str
    name: str
    email: str

class User(UserCreate):
    id: int
    created_at: datetime
