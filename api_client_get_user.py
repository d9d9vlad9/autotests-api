from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.fakers import fake


public_user_client = get_public_users_client()

create_user_request = CreateUserRequestSchema()
create_user_response = public_user_client.create_user(create_user_request)
print("Create user response data:", create_user_response)

authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
private_user_client = get_private_users_client(authentication_user)

get_user_response = private_user_client.get_user(create_user_response.user.id)
print("Get user response data:", get_user_response)
