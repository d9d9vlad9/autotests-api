from clients.api_clients import APIClient
from httpx import Response
from clients.users.users_schema import GetUserResponseSchema, UpdateUserRequestSchema, UpdateUserResponseSchema
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client


class PrivateUsersClient(APIClient):
    """
    Клиент для работы с API пользователей. Методы: GET /api/v1/users/me, GET /api/v1/users/{userId}, PATCH /api/v1/users/{userId}, DELETE /api/v1/users/{userId}.
    """
    def get_users_me_api(self) -> Response:
        """
        Выполняет запрос на получение информации о текущем пользователе.

        :return: Ответ от сервера.
        """
        return self.get("api/v1/users/me")

    def get_user_api(self, user_id: str) -> Response:
        """
        Выполняет запрос на получение информации о пользователе по его ID.

        :param user_id: ID пользователя.
        :return: Ответ от сервера.
        """
        return self.get(f"api/v1/users/{user_id}")

    def update_user_api(self, user_id: str, request: UpdateUserRequestSchema) -> Response:
        """
        Выполняет запрос на обновление информации о пользователе.

        :param user_id: ID пользователя.
        :param request: Данные для обновления.
        :return: Ответ от сервера.
        """
        return self.patch(f"api/v1/users/{user_id}", json=request.model_dump(by_alias=True))

    def delete_user_api(self, user_id: str) -> Response:
        """
        Выполняет запрос на удаление пользователя.

        :param user_id: ID пользователя.
        :return: Ответ от сервера.
        """
        return self.delete(f"api/v1/users/{user_id}")

    def get_user(self, user_id: str) -> GetUserResponseSchema:
        """
        Выполняет запрос на получение информации о пользователе и возвращает ответ в виде словаря.

        :param user_id: ID пользователя.
        :return: Ответ от сервера в виде словаря.
        """
        response = self.get_user_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text)

def get_private_users_client(user: AuthenticationUserSchema) -> PrivateUsersClient:
    """
    Возвращает экземпляр клиента для работы с API пользователей.

    :param user: Данные для аутентификации пользователя.
    :return: Экземпляр PrivateUsersClient.
    """
    return PrivateUsersClient(client=get_private_http_client(user))