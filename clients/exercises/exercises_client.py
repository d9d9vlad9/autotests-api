from clients.api_clients import APIClient
from httpx import Client, Response
from typing import TypedDict


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
    Клиент для работы с API упражнений.
    """
    def __init__(self, client: Client, base_url: str = "http://localhost:8000/api/v1/exercises"):
        super().__init__(client)
        self.base_url = base_url

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Выполняет запрос на получение упражнения по его ID.

        :param query: courseId для получения списка упражнений.
        :return: Ответ от сервера.
        """
        return self.get(self.base_url, params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Выполняет запрос на получение упражнения по его ID.

        :param exercise_id: ID упражнения.
        :return: Ответ от сервера.
        """
        return self.get(f"{self.base_url}/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Выполняет запрос на создание упражнения.

        :param request: Данные для создания упражнения.
        :return: Ответ от сервера.
        """
        return self.post(self.base_url, json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Выполняет запрос на обновление упражнения.

        :param exercise_id: ID упражнения.
        :param request: Данные для обновления упражнения.
        :return: Ответ от сервера.
        """
        return self.patch(f"{self.base_url}/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Выполняет запрос на удаление упражнения.

        :param exercise_id: ID упражнения.
        :return: Ответ от сервера.
        """
        return self.delete(f"{self.base_url}/{exercise_id}")
