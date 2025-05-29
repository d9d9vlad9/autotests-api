import allure
from clients.api_clients import APIClient
from httpx import Response
from clients.public_http_builder import get_public_http_client
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema, RefreshRequestSchema
from tools.routes import APIRoutes


class AuthenticationClient(APIClient):
    """
    Клиент для работы с API аутентификации. Методы: POST /api/v1/authentication/login, POST /api/v1/authentication/refresh.
    """
    @allure.step("Authenticate user")
    def login_api(self, request: LoginRequestSchema) -> Response:
        """
        Выполняет запрос на вход в систему и получение токена доступа.

        :param request: Данные для входа в систему.
        :return: Ответ от сервера.
        """
        return self.post(
            f"{APIRoutes.AUTHENTICATION}/login",
            json=request.model_dump(by_alias=True))

    @allure.step("Refresh authentication token")
    def refresh_api(self, request: RefreshRequestSchema) -> Response:
        """
        Выполняет запрос на обновление токена доступа.

        :param request: Данные для обновления токена.
        :return: Ответ от сервера.
        """
        return self.post(
            f"{APIRoutes.AUTHENTICATION}/refresh",
            json=request.model_dump(by_alias=True))

    def login(self, request: LoginRequestSchema) -> LoginResponseSchema:
        """
        Выполняет запрос на вход в систему и возвращает токен доступа.

        :param request: Данные для входа в систему.
        :return: Авторизационный токен.
        """
        response = self.login_api(request)
        return LoginResponseSchema.model_validate_json(response.text)

def get_authentication_client() -> AuthenticationClient:
    """
    Возвращает экземпляр клиента для работы с API аутентификации.

    :return: Экземпляр AuthenticationClient.
    """
    return AuthenticationClient(client=get_public_http_client())