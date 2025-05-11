from clients.api_clients import APIClient
from httpx import Response
from typing import TypedDict


class CreateUserRequest(TypedDict):
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
    def __init__(self, client):
        super().__init__(client)
        self.base_url = "http://localhost:8000/api/v1/users"

    def create_user_api(self, request: CreateUserRequest) -> Response:
        """
        Выполняет запрос на создание пользователя.

        :param request: Данные для создания пользователя.
        :return: Ответ от сервера.
        """
        return self.post(f"{self.base_url}", json=request)