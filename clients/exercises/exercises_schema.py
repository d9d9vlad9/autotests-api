from pydantic import BaseModel, Field, ConfigDict
from tools.fakers import fake


class Exercise(BaseModel):
    """
    Базовая модель упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)

class ExercisesSchema(BaseModel):
    """
    Тип данных для упражнения.
    """
    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")

class CreateExerciseResponseSchema(Exercise):
    """
    Тип данных для ответа на запрос создания упражнения.
    """
    exercise: ExercisesSchema

class GetExercisesResponseSchema(Exercise):
    """
    Тип данных для ответа на запрос получения упражнения.
    """
    exercise: list[ExercisesSchema]

class GetExercisesQuerySchema(Exercise):
    """
    Тип данных для запроса на получение списка упражнений.
    """
    courseId: str

class CreateExerciseRequestSchema(Exercise):
    """
    Тип данных для запроса на создание упражнения.
    """
    title: str = Field(default_factory=fake.sentence)
    course_id: str = Field(alias="courseId", default_factory=fake.uuid4)
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    order_index: int = Field(alias="orderIndex", default_factory=fake.integer)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)

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
