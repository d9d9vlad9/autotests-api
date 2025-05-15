from pydantic import BaseModel, Field
from tools.fakers import fake


class Exercise(BaseModel):
    """
    Базовая модель упражнения.
    """
    title: str = Field(default_factory=fake.sentence)
    course_id: str = Field(alias="courseId", default_factory=fake.uuid4)
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    order_index: int = Field(alias="orderIndex", default_factory=fake.integer)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)


class ExerciseSchema(Exercise):
    """
    Тип данных для упражнения.
    """
    id: str

class CreateExerciseResponseSchema(BaseModel):
    """
    Тип данных для ответа на запрос создания упражнения.
    """
    exercise: ExerciseSchema

class GetExercisesResponseSchema(BaseModel):
    """
    Тип данных для ответа на запрос получения упражнения.
    """
    exercise: list[ExerciseSchema]

class GetExercisesQuerySchema(BaseModel):
    """
    Тип данных для запроса на получение списка упражнений.
    """
    courseId: str

class CreateExerciseRequestSchema(Exercise):
    """
    Тип данных для запроса на создание упражнения.
    """
    pass

class UpdateExerciseRequestSchema(Exercise):
    """
    Тип данных для запроса на обновление информации об упражнении.
    """
    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int | None = Field(alias="minScore", default_factory=fake.min_score)
    order_index: int | None = Field(alias="orderIndex", default_factory=fake.integer)
    description: str | None = Field(default_factory=fake.text)
    estimated_time: str | None = Field(alias="estimatedTime", default_factory=fake.estimated_time)
