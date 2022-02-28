

from pydantic import BaseModel, EmailStr, constr


class User(BaseModel):
    name: constr(min_length=2, max_length=50)
    email: EmailStr
    password: str