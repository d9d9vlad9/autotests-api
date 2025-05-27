import allure
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from clients.api_clients import APIClient
from clients.public_http_builder import get_public_http_client
from httpx import Response


class PublicUsersClient(APIClient):
    """
    Клиент для работы с API пользователей.
    """

    @allure.step("Create user")
    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Выполняет запрос на создание пользователя.

        :param request: Данные для создания пользователя.
        :return: Ответ от сервера.
        """
        return self.post("/api/v1/users", json=request.model_dump(by_alias=True))

    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        """
        Выполняет запрос на создание пользователя и возвращает ответ в виде словаря.

        :param request: Данные для создания пользователя.
        :return: Ответ от сервера в виде словаря CreateUserResponseDict.
        """
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)

def get_public_users_client() -> PublicUsersClient:
    """
    Возвращает экземпляр клиента для работы с API пользователей.

    :return: Экземпляр PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())