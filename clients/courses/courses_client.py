from clients.api_clients import APIClient
from httpx import Client, Response
from typing import TypedDict


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
    def __init__(self, client: Client, base_url: str = "http://localhost:8000/api/v1/courses"):
        super().__init__(client)
        self.base_url = base_url

    def get_courses_api(self, query: GetCoursesQueryDict) -> Response:
        """
        Выполняет запрос на получение списка курсов.

        :param query: userId.
        :return: Ответ от сервера.
        """
        return self.get(self.base_url, params=query)

    def get_course_api(self, course_id: str) -> Response:
        """
        Выполняет запрос на получение информации о курсе.

        :param course_id: ID курса.
        :return: Ответ от сервера.
        """
        return self.get(f"{self.base_url}/{course_id}")

    def create_course_api(self, request: CreateCourseRequestDict) -> Response:
        """
        Выполняет запрос на создание курса.

        :param request: Данные для создания курса. Словарь с ключами: title, maxScore, minScore, description, estimatedTime, previewFileId, createdByUserId.
        :return: Ответ от сервера.
        """
        return self.post(self.base_url, json=request)

    def update_course_api(self, course_id: str, request: UpdateCourseRequestDict) -> Response:
        """
        Выполняет запрос на обновление информации о курсе.

        :param course_id: ID курса.
        :param request: Данные для обновления курса. Словарь с ключами: title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера.
        """
        return self.patch(f"{self.base_url}/{course_id}", json=request)

    def delete_course_api(self, course_id: str) -> Response:
        """
        Выполняет запрос на удаление курса.

        :param course_id: ID курса.
        :return: Ответ от сервера.
        """
        return self.delete(f"{self.base_url}/{course_id}")