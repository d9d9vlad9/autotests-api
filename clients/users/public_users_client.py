from clients.api_clients import APIClient
from httpx import Client, Response
from typing import TypedDict


class CreateUserRequestDict(TypedDict):
    """
    Тип данных для запроса на создание пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class PublicUsersClient(APIClient):
    """
    Клиент для работы с API пользователей.
    """
    def __init__(self, client: Client, base_url: str = "http://localhost:8000/api/v1/users"):
        super().__init__(client)
        self.base_url = base_url

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Выполняет запрос на создание пользователя.

        :param request: Данные для создания пользователя.
        :return: Ответ от сервера.
        """
        return self.post(self.base_url, json=request)