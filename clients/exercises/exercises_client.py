from clients.api_clients import APIClient
from httpx import Response
from typing import TypedDict, List
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema


class Exercise(TypedDict):
    """
    Тип данных для упражнения.
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class CreateExerciseResponseDict(TypedDict):
    """
    Тип данных для ответа на запрос создания упражнения.
    """
    exercise: Exercise

class GetExercisesResponseDict(TypedDict):
    """
    Тип данных для ответа на запрос получения упражнения.
    """
    exercise: List[Exercise]

class GetExercisesQueryDict(TypedDict):
    """
    Тип данных для запроса на получение списка упражнений.
    """
    courseId: str

class CreateExerciseRequestDict(TypedDict):
    """
    Тип данных для запроса на создание упражнения.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class UpdateExerciseRequestDict(TypedDict):
    """
    Тип данных для запроса на обновление информации об упражнении.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class ExercisesClient(APIClient):
    """
    Клиент для работы с API упражнений. Методы: GET /api/v1/exercises, GET /api/v1/exercises/{exerciseId}, POST /api/v1/exercises, PATCH /api/v1/exercises/{exerciseId}, DELETE /api/v1/exercises/{exerciseId}.
    """
    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Выполняет запрос на получение упражнения по его ID.

        :param query: courseId для получения списка упражнений.
        :return: Ответ от сервера.
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Выполняет запрос на получение упражнения по его ID.

        :param exercise_id: ID упражнения.
        :return: Ответ от сервера.
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Выполняет запрос на создание упражнения.

        :param request: Данные для создания упражнения.
        :return: Ответ от сервера.
        """
        return self.post('/api/v1/exercises', json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Выполняет запрос на обновление упражнения.

        :param exercise_id: ID упражнения.
        :param request: Данные для обновления упражнения.
        :return: Ответ от сервера.
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Выполняет запрос на удаление упражнения.

        :param exercise_id: ID упражнения.
        :return: Ответ от сервера.
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercise(self, exercise_id: str) -> CreateExerciseResponseDict:
        """
        Выполняет запрос на получение упражнения по его ID.

        :param exercise_id: ID упражнения.
        :return: Данные упражнения.
        """
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        """
        Выполняет запрос на получение списка упражнений.

        :param query: courseId для получения списка упражнений.
        :return: Список упражнений.
        """
        response = self.get_exercises_api(query)
        return response.json()

    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExerciseResponseDict:
        """
        Выполняет запрос на создание упражнения и возвращает объект созданного упражнения.

        :param request: Данные для создания упражнения.
        :return: CreateExerciseResponseDict с информацией о созданном упражнении.
        """
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestDict) -> CreateExerciseResponseDict:
        """
        Выполняет запрос на обновление упражнения и возвращает объект обновленного упражнения.

        :param exercise_id: ID упражнения.
        :param request: Данные для обновления упражнения.
        :return: CreateExerciseResponseDict с информацией об обновленном упражнении.
        """
        response = self.update_exercise_api(exercise_id, request)
        return response.json()


def get_exercise_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Возвращает экземпляр клиента для работы с API курсов.

    :return: Экземпляр CoursesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))