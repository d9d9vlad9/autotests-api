from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import get_random_email
import jsonschema

public_user_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)
create_user_response = public_user_client.create_user_api(create_user_request)
create_user_request_schema = CreateUserResponseSchema.model_json_schema()

validate_json_schema(instance=create_user_response.json(), schema=create_user_request_schema)

jsonschema.validate(instance=create_user_response.json(), schema=create_user_request_schema)