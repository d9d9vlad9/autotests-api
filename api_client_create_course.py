from clients.courses.courses_client import get_courses_client
from clients.files.files_client import get_files_client
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.users.users_schema import CreateUserRequestSchema
from clients.courses.courses_schema import CreateCourseRequestSchema
from config import settings


public_user_client = get_public_users_client()

create_user_request = CreateUserRequestSchema()
create_user_response = public_user_client.create_user(create_user_request)

authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
files_client = get_files_client(authentication_user)
course_client = get_courses_client(authentication_user)

create_file_request = CreateFileRequestSchema(upload_file=settings.test_data.image_png_file)
create_file_response = files_client.create_file(create_file_request)
print("Create file data:", create_file_response)

create_course_request = CreateCourseRequestSchema(
    previewFileId=create_file_response.file.id,
    createdByUserId=create_user_response.user.id
)
create_course_response = course_client.create_course(create_course_request)
print("Create course data:", create_course_response)