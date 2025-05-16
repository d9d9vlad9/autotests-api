import pytest
from pydantic import BaseModel, EmailStr
from clients.authentication.authentication_client import AuthenticationClient, get_authentication_client
from clients.users.public_users_client import PublicUsersClient, get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema


class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> EmailStr:
        """
        Возвращает email пользователя.
        :return: Email пользователя.
        """
        return self.request.email

    @property
    def password(self) -> str:
        """
        Возвращает пароль пользователя.
        :return: Пароль пользователя.
        """
        return self.request.password


@pytest.fixture
def authentication_client() -> AuthenticationClient:
    return get_authentication_client()

@pytest.fixture
def public_users_client() -> PublicUsersClient:
    return get_public_users_client()

@pytest.fixture
def function_user(public_users_client: PublicUsersClient) -> UserFixture:
    """
    Функция для создания пользователя.
    :param public_users_client: Клиент для работы с API пользователей.
    :return: Созданный пользователь.
    """
    request = CreateUserRequestSchema()
    responses = public_users_client.create_user(request)
    return UserFixture(request=request, response=responses)