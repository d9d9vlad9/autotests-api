from clients.api_clients import APIClient
from httpx import Client, Response
from typing import TypedDict

class LoginRequestDict(TypedDict):
    """
    Тип данных для запроса на вход в систему.
    """
    email: str
    password: str

class RefreshRequestDict(TypedDict):
    """
    Тип данных для запроса на обновление токена.
    """
    refreshToken: str

class AuthenticationClient(APIClient):
    """
    Клиент для работы с API аутентификации.
    """
    def __init__(self, client: Client, base_url: str = "http://localhost:8000/api/v1/authentication"):
        super().__init__(client)
        self.base_url = base_url

    def login_api(self, request: LoginRequestDict) -> Response:
        """
        Выполняет запрос на вход в систему и получение токена доступа.

        :param request: Данные для входа в систему.
        :return: Ответ от сервера.
        """
        return self.post(f"{self.base_url}/login", json=request)

    def refresh_api(self, request: RefreshRequestDict) -> Response:
        """
        Выполняет запрос на обновление токена доступа.

        :param request: Данные для обновления токена.
        :return: Ответ от сервера.
        """
        return self.post(f"{self.base_url}/refresh", json=request)