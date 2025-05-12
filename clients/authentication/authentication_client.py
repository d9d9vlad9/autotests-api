from clients.api_clients import APIClient
from httpx import Response
from typing import TypedDict
from clients.public_http_builder import get_public_http_client

class Token(TypedDict):
    """
    Тип данных для токена доступа.
    """
    tokenType: str
    accessToken: str
    refreshToken: str

class LoginRequestDict(TypedDict):
    """
    Тип данных для запроса на вход в систему.
    """
    email: str
    password: str

class LoginResponseDict(TypedDict):
    """
    Тип данных для ответа на запрос входа в систему.
    """
    token: Token

class RefreshRequestDict(TypedDict):
    """
    Тип данных для запроса на обновление токена.
    """
    refreshToken: str

class AuthenticationClient(APIClient):
    """
    Клиент для работы с API аутентификации. Методы: POST /api/v1/authentication/login, POST /api/v1/authentication/refresh.
    """
    def login_api(self, request: LoginRequestDict) -> Response:
        """
        Выполняет запрос на вход в систему и получение токена доступа.

        :param request: Данные для входа в систему.
        :return: Ответ от сервера.
        """
        return self.post("/api/v1/authentication/login", json=request)

    def refresh_api(self, request: RefreshRequestDict) -> Response:
        """
        Выполняет запрос на обновление токена доступа.

        :param request: Данные для обновления токена.
        :return: Ответ от сервера.
        """
        return self.post("/api/v1/authentication/refresh", json=request)

    def login(self, request: LoginRequestDict) -> LoginResponseDict:
        """
        Выполняет запрос на вход в систему и возвращает токен доступа.

        :param request: Данные для входа в систему.
        :return: Авторизационный токен.
        """
        response = self.login_api(request)
        return response.json()

def get_authentication_client() -> AuthenticationClient:
    """
    Возвращает экземпляр клиента для работы с API аутентификации.

    :return: Экземпляр AuthenticationClient.
    """
    return AuthenticationClient(client=get_public_http_client())