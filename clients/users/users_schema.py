from pydantic import BaseModel, Field, ConfigDict, EmailStr
from tools.fakers import fake


class UserSchema(BaseModel):
    """
    Тип данных для пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserRequestSchema(BaseModel):
    """
    Тип данных для запроса на создание пользователя. Метод POST /api/v1/users.
    """
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr | str = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)
    last_name: str = Field(alias="lastName", default_factory=fake.last_name)
    first_name: str = Field(alias="firstName", default_factory=fake.first_name)
    middle_name: str = Field(alias="middleName", default_factory=fake.middle_name)

class CreateUserResponseSchema(BaseModel):
    """
    Тип данных для ответа на запрос создания пользователя.
    """
    user: UserSchema

class UpdateUserRequestSchema(BaseModel):
    """
    Тип данных для запроса на обновление информации о пользователе.
    """
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr | None = Field(default_factory=fake.email)
    last_name: str | None = Field(alias="lastName", default_factory=fake.last_name)
    first_name: str | None = Field(alias="firstName", default_factory=fake.first_name)
    middle_name: str | None = Field(alias="middleName", default_factory=fake.middle_name)


class UpdateUserResponseSchema(BaseModel):
    """
    Тип данных для ответа на запрос обновления информации о пользователе.
    """
    user: UserSchema

class GetUserResponseSchema(BaseModel):
    """
    Тип данных для ответа на запрос получения информации о пользователе.
    """
    user: UserSchema
