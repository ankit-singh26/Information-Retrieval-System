from pydantic import BaseModel

class User(BaseModel):
    email: str
    password: str

class Question(BaseModel):
    query: str
