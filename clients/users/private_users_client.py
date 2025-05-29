import allure
from clients.api_clients import APIClient
from httpx import Response
from clients.users.users_schema import GetUserResponseSchema, UpdateUserRequestSchema, UpdateUserResponseSchema
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from tools.routes import APIRoutes


class PrivateUsersClient(APIClient):
    """
    Клиент для работы с API пользователей. Методы: GET /api/v1/users/me, GET /api/v1/users/{userId}, PATCH /api/v1/users/{userId}, DELETE /api/v1/users/{userId}.
    """
    @allure.step("Get user me")
    def get_users_me_api(self) -> Response:
        """
        Выполняет запрос на получение информации о текущем пользователе.

        :return: Ответ от сервера.
        """
        return self.get("api/v1/users/me")

    @allure.step("Get user by id {user_id}")
    def get_user_api(self, user_id: str) -> Response:
        """
        Выполняет запрос на получение информации о пользователе по его ID.

        :param user_id: ID пользователя.
        :return: Ответ от сервера.
        """
        return self.get(f"{APIRoutes.USERS}/{user_id}")

    @allure.step("Update user by id {user_id}")
    def update_user_api(self, user_id: str, request: UpdateUserRequestSchema) -> Response:
        """
        Выполняет запрос на обновление информации о пользователе.

        :param user_id: ID пользователя.
        :param request: Данные для обновления.
        :return: Ответ от сервера.
        """
        return self.patch(f"{APIRoutes.USERS}/{user_id}", json=request.model_dump(by_alias=True))

    @allure.step("Delete user by id {user_id}")
    def delete_user_api(self, user_id: str) -> Response:
        """
        Выполняет запрос на удаление пользователя.

        :param user_id: ID пользователя.
        :return: Ответ от сервера.
        """
        return self.delete(f"{APIRoutes.USERS}/{user_id}")

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