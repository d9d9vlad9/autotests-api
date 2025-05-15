from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.private_users_client import get_private_users_client
from clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema
from tools.fakers import fake
from tools.assertions.schema import validate_json_schema

public_user_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=fake.email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)

create_user_response = public_user_client.create_user(create_user_request)


authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
private_user_client = get_private_users_client(authentication_user)
get_user_response = private_user_client.get_user_api(create_user_response.user.id)
create_user_request_schema = GetUserResponseSchema.model_json_schema()

validate_json_schema(instance=get_user_response.json(), schema=create_user_request_schema)
