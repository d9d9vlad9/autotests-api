from clients.api_clients import APIClient
from httpx import Response
from typing import TypedDict

class UpdateUserRequestDict(TypedDict):
    """
    Тип данных для запроса на обновление информации о пользователе.
    """
    email: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None


class PrivateUsersClient(APIClient):
    """
    Клиент для работы с API пользователей.
    """
    def __init__(self, client):
        super().__init__(client)
        self.base_url = "http://localhost:8000/api/v1/users"

    def get_users_me_api(self) -> Response:
        """
        Выполняет запрос на получение информации о текущем пользователе.

        :return: Ответ от сервера.
        """
        return self.get(f"{self.base_url}/me")

    def get_user_api(self, user_id: str) -> Response:
        """
        Выполняет запрос на получение информации о пользователе по его ID.

        :param user_id: ID пользователя.
        :return: Ответ от сервера.
        """
        return self.get(f"{self.base_url}/{user_id}")

    def update_user_api(self, user_id: str, request) -> Response:
        """
        Выполняет запрос на обновление информации о пользователе.

        :param user_id: ID пользователя.
        :param request: Данные для обновления.
        :return: Ответ от сервера.
        """
        return self.patch(f"{self.base_url}/{user_id}", json=request)

    def delete_user_api(self, user_id: str) -> Response:
        """
        Выполняет запрос на удаление пользователя.

        :param user_id: ID пользователя.
        :return: Ответ от сервера.
        """
        return self.delete(f"{self.base_url}/{user_id}")