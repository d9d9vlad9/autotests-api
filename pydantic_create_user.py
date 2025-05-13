from pydantic import BaseModel, EmailStr, Field
from uuid import uuid4
from tools.fakers import get_random_email


class User(BaseModel):
    """
    Базовая модель пользователя.
    """
    email: EmailStr = Field(default=get_random_email())
    last_name: str = Field(alias="lastName", default="Doe")
    first_name: str = Field(alias="firstName", default="John")
    middle_name: str = Field(alias="middleName", default="Q")

class UserSchema(User):
    """
    UserSchema — модель данных пользователя
    """
    id: str = Field(default_factory=lambda: str(uuid4()))

class CreateUserRequestSchema(User):
    """
    CreateUserRequestSchema — модель данных для создания пользователя
    """
    password: str = Field(default="password")

class CreateUserResponseSchema(BaseModel):
    """
    CreateUserResponseSchema — модель данных ответа на создание пользователя
    """
    user: UserSchema = Field(default_factory=UserSchema)
