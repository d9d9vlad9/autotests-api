import allure
from httpx import Response
from clients.api_clients import APIClient
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from clients.courses.courses_schema import GetCoursesQuerySchema, UpdateCourseRequestSchema, CreateCourseResponseSchema, CreateCourseRequestSchema
from clients.api_coverage import tracker
from tools.routes import APIRoutes


class CoursesClient(APIClient):
    """
    Клиент для работы с API курсов. Методы: GET /api/v1/courses, GET /api/v1/courses/{courseId}, POST /api/v1/courses, PATCH /api/v1/courses/{courseId}, DELETE /api/v1/courses/{courseId}.
    """
    @allure.step("Get courses")
    @tracker.track_coverage_httpx(APIRoutes.COURSES)
    def get_courses_api(self, query: GetCoursesQuerySchema) -> Response:
        """
        Выполняет запрос на получение списка курсов.

        :param query: userId.
        :return: Ответ от сервера.
        """
        return self.get(APIRoutes.COURSES, params=query.model_dump(by_alias=True))

    @allure.step("Get course by id {course_id}")
    @tracker.track_coverage_httpx(f"{APIRoutes.COURSES}/{{course_id}}")
    def get_course_api(self, course_id: str) -> Response:
        """
        Выполняет запрос на получение информации о курсе.

        :param course_id: ID курса.
        :return: Ответ от сервера.
        """
        return self.get(f"{APIRoutes.COURSES}/{course_id}")

    @allure.step("Create course")
    @tracker.track_coverage_httpx(APIRoutes.COURSES)
    def create_course_api(self, request: CreateCourseRequestSchema) -> Response:
        """
        Выполняет запрос на создание курса.

        :param request: Данные для создания курса. Словарь с ключами: title, maxScore, minScore, description, estimatedTime, previewFileId, createdByUserId.
        :return: Ответ от сервера.
        """
        return self.post(APIRoutes.COURSES, json=request.model_dump(by_alias=True))

    @allure.step("Update course by id {course_id}")
    @tracker.track_coverage_httpx(f"{APIRoutes.COURSES}/{{course_id}}")
    def update_course_api(self, course_id: str, request: UpdateCourseRequestSchema) -> Response:
        """
        Выполняет запрос на обновление информации о курсе.

        :param course_id: ID курса.
        :param request: Данные для обновления курса. Словарь с ключами: title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера.
        """
        return self.patch(f"{APIRoutes.COURSES}/{course_id}", json=request.model_dump(by_alias=True))

    @allure.step("Delete course by id {course_id}")
    @tracker.track_coverage_httpx(f"{APIRoutes.COURSES}/{{course_id}}")
    def delete_course_api(self, course_id: str) -> Response:
        """
        Выполняет запрос на удаление курса.

        :param course_id: ID курса.
        :return: Ответ от сервера.
        """
        return self.delete(f"{APIRoutes.COURSES}/{course_id}")

    def create_course(self, request: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        """
        Выполняет запрос на создание курса и возвращает ID созданного курса.

        :param request: Данные для создания курса.
        :return: ID созданного курса.
        """
        response = self.create_course_api(request)
        return CreateCourseResponseSchema.model_validate_json(response.text)

def get_courses_client(user: AuthenticationUserSchema) -> CoursesClient:
    """
    Возвращает экземпляр клиента для работы с API курсов.

    :return: Экземпляр CoursesClient.
    """
    return CoursesClient(client=get_private_http_client(user))