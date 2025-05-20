import pytest
from pydantic import BaseModel

from clients.exercises.exercises_client import ExercisesClient, get_exercise_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from fixtures.courses import CourseFixture
from fixtures.users import UserFixture


class ExerciseFixture(BaseModel):
    """
    Класс для создания упражнения.
    """
    request: CreateExerciseRequestSchema
    response: CreateExerciseResponseSchema

@pytest.fixture
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    """
    Функция для создания клиента для работы с упражнениями.
    :param function_user: Созданный пользователь.
    :return: Клиент для работы с упражнениями.
    """
    return get_exercise_client(function_user.authentication_user)

@pytest.fixture
def function_exercise(
        exercises_client: ExercisesClient,
        function_course: CourseFixture,
) -> ExerciseFixture:
    """
    Функция для создания упражнения.
    :param exercises_client: Клиент для работы с упражнениями.
    :param function_course: Созданный курс.
    :return: Модель запроса и ответа на создание упражнения.
    """
    request = CreateExerciseRequestSchema()
    response = exercises_client.create_exercise(request)
    return ExerciseFixture(request=request, response=response)
