from pydantic import BaseModel, field_validator
from typing import Optional


class CreateUser(BaseModel):
    name: str
    password: str

    @field_validator('password')
    def secure_password(cls, value):
        if len(value) < 5:
            raise ValueError(f'password is to short')


class UpdateUser(BaseModel):
    name: Optional[str]
    password: Optional[str]

    @field_validator('password')
    def secure_password(cls, value):
        if len(value) < 5:
            raise ValueError(f'Пароль слишком короткий')