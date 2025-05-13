from pydantic import BaseModel, Field



class Exercise(BaseModel):
    """
    Базовая модель упражнения.
    """
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


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
    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int | None = Field(alias="orderIndex")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")