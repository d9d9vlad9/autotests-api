import allure
from clients.api_clients import APIClient
from httpx import Response
from clients.exercises.exercises_schema import GetExercisesQuerySchema, UpdateExerciseRequestSchema, CreateExerciseResponseSchema, CreateExerciseRequestSchema, GetExercisesResponseSchema
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from tools.routes import APIRoutes


class ExercisesClient(APIClient):
    """
    Клиент для работы с API упражнений. Методы: GET /api/v1/exercises, GET /api/v1/exercises/{exerciseId}, POST /api/v1/exercises, PATCH /api/v1/exercises/{exerciseId}, DELETE /api/v1/exercises/{exerciseId}.
    """
    @allure.step("Get exercises")
    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Выполняет запрос на получение списка упражнений.

        :param query: courseId для получения списка упражнений.
        :return: Ответ от сервера.
        """
        return self.get(APIRoutes.EXERCISES, params=query.model_dump(by_alias=True))

    @allure.step("Get exercise by id {exercise_id}")
    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Выполняет запрос на получение упражнения по его ID.

        :param exercise_id: ID упражнения.
        :return: Ответ от сервера.
        """
        return self.get(f"{APIRoutes.EXERCISES}/{exercise_id}")

    @allure.step("Create exercise")
    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Выполняет запрос на создание упражнения.

        :param request: Данные для создания упражнения.
        :return: Ответ от сервера.
        """
        return self.post(APIRoutes.EXERCISES, json=request.model_dump(by_alias=True))

    @allure.step("Update exercise by id {exercise_id}")
    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
        Выполняет запрос на обновление упражнения.

        :param exercise_id: ID упражнения.
        :param request: Данные для обновления упражнения.
        :return: Ответ от сервера.
        """
        return self.patch(f"{APIRoutes.EXERCISES}/{exercise_id}", json=request.model_dump(by_alias=True))

    @allure.step("Delete exercise by id {exercise_id}")
    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Выполняет запрос на удаление упражнения.

        :param exercise_id: ID упражнения.
        :return: Ответ от сервера.
        """
        return self.delete(f"{APIRoutes.EXERCISES}/{exercise_id}")

    def get_exercise(self, exercise_id: str) -> CreateExerciseResponseSchema:
        """
        Выполняет запрос на получение упражнения по его ID.

        :param exercise_id: ID упражнения.
        :return: Данные упражнения.
        """
        response = self.get_exercise_api(exercise_id)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        """
        Выполняет запрос на получение списка упражнений.

        :param query: courseId для получения списка упражнений.
        :return: Список упражнений.
        """
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        """
        Выполняет запрос на создание упражнения и возвращает объект созданного упражнения.

        :param request: Данные для создания упражнения.
        :return: CreateExerciseResponseDict с информацией о созданном упражнении.
        """
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        """
        Выполняет запрос на обновление упражнения и возвращает объект обновленного упражнения.

        :param exercise_id: ID упражнения.
        :param request: Данные для обновления упражнения.
        :return: CreateExerciseResponseDict с информацией об обновленном упражнении.
        """
        response = self.update_exercise_api(exercise_id, request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)


def get_exercise_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Возвращает экземпляр клиента для работы с API курсов.

    :return: Экземпляр CoursesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))