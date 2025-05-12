from clients.api_clients import APIClient
from httpx import Response
from typing import TypedDict
from clients.files.files_client import File
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client
from clients.users.private_users_client import User


class Course(TypedDict):
    """
    Тип данных для курса.
    """
    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    previewFile: File
    estimatedTime: str
    createdByUser: User

class CreateCourseResponseDict(TypedDict):
    """
    Тип данных для ответа на запрос создания курса.
    """
    course: Course

class GetCoursesQueryDict(TypedDict):
    """
    Тип данных для запроса на получение списка курсов.
    """
    userId: str

class CreateCourseRequestDict(TypedDict):
    """
    Тип данных для запроса на создание курса.
    """
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str

class UpdateCourseRequestDict(TypedDict):
    """
    Тип данных для запроса на обновление информации о курсе.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None

class CoursesClient(APIClient):
    """
    Клиент для работы с API курсов. Методы: GET /api/v1/courses, GET /api/v1/courses/{courseId}, POST /api/v1/courses, PATCH /api/v1/courses/{courseId}, DELETE /api/v1/courses/{courseId}.
    """
    def get_courses_api(self, query: GetCoursesQueryDict) -> Response:
        """
        Выполняет запрос на получение списка курсов.

        :param query: userId.
        :return: Ответ от сервера.
        """
        return self.get("/api/v1/courses", params=query)

    def get_course_api(self, course_id: str) -> Response:
        """
        Выполняет запрос на получение информации о курсе.

        :param course_id: ID курса.
        :return: Ответ от сервера.
        """
        return self.get(f"/api/v1/courses/{course_id}")

    def create_course_api(self, request: CreateCourseRequestDict) -> Response:
        """
        Выполняет запрос на создание курса.

        :param request: Данные для создания курса. Словарь с ключами: title, maxScore, minScore, description, estimatedTime, previewFileId, createdByUserId.
        :return: Ответ от сервера.
        """
        return self.post("/api/v1/courses", json=request)

    def update_course_api(self, course_id: str, request: UpdateCourseRequestDict) -> Response:
        """
        Выполняет запрос на обновление информации о курсе.

        :param course_id: ID курса.
        :param request: Данные для обновления курса. Словарь с ключами: title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера.
        """
        return self.patch(f"/api/v1/courses/{course_id}", json=request)

    def delete_course_api(self, course_id: str) -> Response:
        """
        Выполняет запрос на удаление курса.

        :param course_id: ID курса.
        :return: Ответ от сервера.
        """
        return self.delete(f"/api/v1/courses/{course_id}")

    def create_course(self, request: CreateCourseRequestDict) -> CreateCourseResponseDict:
        """
        Выполняет запрос на создание курса и возвращает ID созданного курса.

        :param request: Данные для создания курса.
        :return: ID созданного курса.
        """
        response = self.create_course_api(request)
        return response.json()

def get_courses_client(user: AuthenticationUserDict) -> CoursesClient:
    """
    Возвращает экземпляр клиента для работы с API курсов.

    :return: Экземпляр CoursesClient.
    """
    return CoursesClient(client=get_private_http_client(user))