from pydantic import BaseModel, Field, ConfigDict
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema


class Course(BaseModel):
    """
    Базовая модель курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")

class CourseSchema(Course):
    """
    CourseSchema — модель данных курса
    """
    id: str
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
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias="userId")

class CreateCourseRequestSchema(Course):
    """
    Тип данных для запроса на создание курса.
    """
    preview_file_id: str = Field(alias="previewFileId")
    created_by_user_id: str = Field(alias="createdByUserId")

class UpdateCourseRequestSchema(Course):
    """
    Тип данных для запроса на обновление информации о курсе.
    """
    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")
