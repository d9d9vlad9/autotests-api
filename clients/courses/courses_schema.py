from pydantic import BaseModel, Field, ConfigDict
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema
from tools.fakers import fake


class Course(BaseModel):
    """
    Базовая модель курса.
    """
    model_config = ConfigDict(populate_by_name=True)

class CourseSchema(Course):
    """
    CourseSchema — модель данных курса
    """
    id: str
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")
    preview_file: FileSchema = Field(alias="previewFile")
    created_by_user: UserSchema = Field(alias="createdByUser")

class CreateCourseResponseSchema(BaseModel):
    """
    Тип данных для ответа на запрос создания курса.
    """
    course: CourseSchema

class GetCoursesQuerySchema(BaseModel):
    """
    Тип данных для запроса на получение списка курсов.
    """
    user_id: str = Field(alias="userId")

class GetCoursesResponseSchema(BaseModel):
    courses: list[CourseSchema]

class CreateCourseRequestSchema(Course):
    """
    Тип данных для запроса на создание курса.
    """
    title: str = Field(default_factory=fake.sentence)
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)
    preview_file_id: str = Field(alias="previewFileId", default_factory=fake.uuid4)
    created_by_user_id: str = Field(alias="createdByUserId", default_factory=fake.uuid4)

class UpdateCourseRequestSchema(Course):
    """
    Тип данных для запроса на обновление информации о курсе.
    """
    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int | None = Field(alias="minScore", default_factory=fake.min_score)
    description: str | None = Field(default_factory=fake.text)
    estimated_time: str | None = Field(alias="estimatedTime", default_factory=fake.estimated_time)

class UpdateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа обновления курса.
    """
    course: CourseSchema
