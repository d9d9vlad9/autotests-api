from pydantic import BaseModel, HttpUrl, Field, FilePath
from tools.fakers import fake


class FileSchema(BaseModel):
    """
    Тип данных для файла.
    """
    id: str
    url: HttpUrl
    filename: str
    directory: str

class CreateFileRequestSchema(BaseModel):
    """
    Тип данных для запроса на создание файла.
    """
    filename: str = Field(default_factory=lambda: f"file_{fake.uuid4()}.txt")
    directory: str = Field(default="tests")
    upload_file: FilePath

class CreateFileResponseSchema(BaseModel):
    """
    Тип данных для ответа на запрос создания файла.
    """
    file: FileSchema

class GetFileResponseSchema(BaseModel):
    """
    Тип данных для ответа на запрос получения файла.
    """
    file: FileSchema