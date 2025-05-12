from httpx import Client

from clients.authentication.authentication_client import get_authentication_client, LoginRequestDict
from typing import TypedDict

class AuthenticationUserDict(TypedDict):
    """
    Тип данных для пользователя аутентификации.
    """
    email: str
    password: str

def get_private_http_client(user: AuthenticationUserDict) -> Client:
    """
    Создает и возвращает экземпляр httpx.Client с настройками для приватного HTTP-клиента.
    :param user: Данные пользователя для аутентификации.
    :return: Экземпляр httpx.Client с заголовком авторизации.
    """
    authentication_client = get_authentication_client()

    login_request = LoginRequestDict(email=user['email'], password=user['password'])
    login_response = authentication_client.login(login_request)

    return Client(
        timeout=5,
        base_url="http://localhost:8000",
        headers={"Authorization": f"Bearer {login_response['token']['accessToken']}"}
    )