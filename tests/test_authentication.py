from http import HTTPStatus
from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginResponseSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema



def test_login():
    public_client = get_public_users_client()
    create_req = CreateUserRequestSchema()

    public_client.create_user(create_req)

    auth_user = AuthenticationUserSchema(
        email=create_req.email,
        password=create_req.password
    )
    auth_client = get_authentication_client()
    login_response = auth_client.login_api(auth_user)
    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)

    assert_status_code(login_response.status_code, HTTPStatus.OK)

    login_data = LoginResponseSchema.model_validate_json(login_response.text)
    validate_json_schema(login_response.json(), login_response_data.model_json_schema())

    # Шаг 5: проверка тела ответа
    assert_login_response(login_data)



