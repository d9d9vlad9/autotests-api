import allure
from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_schema import CreateExerciseResponseSchema, CreateExerciseRequestSchema, \
    ExercisesSchema, UpdateExerciseResponseSchema, UpdateExerciseRequestSchema, GetExercisesResponseSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.errors import assert_internal_error_response
from tools.logger import get_logger


logger = get_logger("EXERCISE_ASSERTIONS")

@allure.step("Check create exercise response")
def assert_create_exercise_response(
        response: CreateExerciseResponseSchema,
        request: CreateExerciseRequestSchema
):
    """
    Проверяет, что ответ на создание упражнения соответствует ожидаемым данным.

    :param response: Фактический ответ от API при создании упражнения.
    :param request: Исходный запрос на создание упражнения.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    logger.info("Check create exercise response")

    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.course_id, request.course_id, "courseId")
    assert_equal(response.exercise.max_score, request.max_score, "maxScore")
    assert_equal(response.exercise.min_score, request.min_score, "minScore")
    assert_equal(response.exercise.order_index, request.order_index, "orderIndex")
    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, "estimatedTime")

@allure.step("Check exercise")
def assert_exercise(
        actual: ExercisesSchema,
        expected: ExercisesSchema
):
    """
    Проверяет, что фактические данные упражнения соответствуют ожидаемым.

    :param actual: Фактические данные упражнения.
    :param expected: Ожидаемые данные упражнения.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check exercise")

    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "courseId")
    assert_equal(actual.max_score, expected.max_score, "maxScore")
    assert_equal(actual.min_score, expected.min_score, "minScore")
    assert_equal(actual.order_index, expected.order_index, "orderIndex")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimatedTime"
)

@allure.step("Check get exercise response")
def assert_get_exercise_response(
        get_exercise_response: CreateExerciseResponseSchema,
        create_exercise_response: CreateExerciseResponseSchema
):
    """
    Проверяет, что ответ на получение упражнения соответствует ответу на его создание.

    :param get_exercise_response: Ответ API при запросе данных упражнения.
    :param create_exercise_response: Ответ API при создании упражнения.
    :raises AssertionError: Если данные упражнения не совпадают.
    """
    logger.info("Check get exercise response")

    assert_exercise(get_exercise_response.exercise, create_exercise_response.exercise)

@allure.step("Check update exercise response")
def assert_update_exercise_response(request: UpdateExerciseRequestSchema, response: UpdateExerciseResponseSchema):
    """
    Проверяет, что ответ на обновление упражнения соответствует данным из запроса.

    :param request: Исходный запрос на обновление упражнения.
    :param response: Ответ API с обновленными данными упражнения.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check update exercise response")

    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.max_score, request.max_score, "maxScore")
    assert_equal(response.exercise.min_score, request.min_score, "minScore")
    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, "estimatedTime")
    assert_equal(response.exercise.order_index, request.order_index, "orderIndex")

@allure.step("Check exercise not found response")
def assert_exercise_not_found_response(actual: InternalErrorResponseSchema):
    """
    Проверяет, что ответ на запрос несуществующего упражнения соответствует ожидаемому ответу об ошибке 404.

    :param actual: Ответ от API с ошибкой, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    logger.info("Check exercise not found response")

    expected = InternalErrorResponseSchema(details="Exercise not found")
    assert_internal_error_response(actual, expected)

@allure.step("Check get exercises response")
def assert_get_exercises_response(
        get_exercise_response: GetExercisesResponseSchema,
        create_exercise_responses: list[CreateExerciseResponseSchema]
):
    """
    Проверяет что ответ на получение списка заданий соответствует ответам на их создание.

    :param get_exercise_response: Ответ API при запросе списка заданий.
    :param create_exercise_responses: Список API ответов при создании заданий.
    :raises AssertionError: Если данные заданий не совпадают.
    """
    logger.info("Check get exercises response")

    assert_length(get_exercise_response.exercises, create_exercise_responses, "courses")

    for index, create_exercise_response in enumerate(create_exercise_responses):
        assert_exercise(get_exercise_response.exercises[index], create_exercise_response.exercise)