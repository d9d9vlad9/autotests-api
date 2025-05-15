from pydantic import BaseModel, Field
from tools.fakers import fake


class TokenSchema(BaseModel):
    """
    Тип данных для токена доступа.
    """
    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")

class LoginRequestSchema(BaseModel):
    """
    Тип данных для запроса на вход в систему.
    """
    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)

class LoginResponseSchema(BaseModel):
    """
    Тип данных для ответа на запрос входа в систему.
    """
    token: TokenSchema

class RefreshRequestSchema(BaseModel):
    """
    Тип данных для запроса на обновление токена.
    """
    refresh_token: str = Field(alias="refreshToken", default_factory=fake.sentence)

print(LoginRequestSchema())