from httpx import Client
from pydantic import BaseModel, EmailStr
from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema
from functools import lru_cache


class AuthenticationUserSchema(BaseModel, frozen=True):
    """
    Тип данных для пользователя аутентификации.
    """
    email: EmailStr
    password: str

@lru_cache(maxsize=None)
def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    """
    Создает и возвращает экземпляр httpx.Client с настройками для приватного HTTP-клиента.
    :param user: Данные пользователя для аутентификации.
    :return: Экземпляр httpx.Client с заголовком авторизации.
    """
    authentication_client = get_authentication_client()

    login_request = LoginRequestSchema(email=user.email, password=user.password)
    login_response = authentication_client.login(login_request)

    return Client(
        timeout=5,
        base_url="http://localhost:8000",
        headers={"Authorization": f"Bearer {login_response.token.access_token}"}
    )