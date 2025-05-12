from typing import TypedDict
from clients.api_clients import APIClient
from clients.public_http_builder import get_public_http_client
from httpx import Response

class User(TypedDict):
    """
    Тип данных для пользователя.
    """
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str

class CreateUserRequestDict(TypedDict):
    """
    Тип данных для запроса на создание пользователя. Метод POST /api/v1/users.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class CreateUserResponseDict(TypedDict):
    """
    Тип данных для ответа на запрос создания пользователя.
    """
    user: User

class PublicUsersClient(APIClient):
    """
    Клиент для работы с API пользователей.
    """
    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Выполняет запрос на создание пользователя.

        :param request: Данные для создания пользователя.
        :return: Ответ от сервера.
        """
        return self.post("/api/v1/users", json=request)

    def create_user(self, request: CreateUserRequestDict) -> CreateUserResponseDict:
        """
        Выполняет запрос на создание пользователя и возвращает ответ в виде словаря.

        :param request: Данные для создания пользователя.
        :return: Ответ от сервера в виде словаря CreateUserResponseDict.
        """
        response = self.create_user_api(request)
        return response.json()

def get_public_users_client() -> PublicUsersClient:
    """
    Возвращает экземпляр клиента для работы с API пользователей.

    :return: Экземпляр PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())