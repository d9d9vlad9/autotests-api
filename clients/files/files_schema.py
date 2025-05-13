from pydantic import BaseModel, HttpUrl


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
    filename: str
    directory: str
    upload_file: str

class CreateFileResponseSchema(BaseModel):
    """
    Тип данных для ответа на запрос создания файла.
    """
    file: FileSchema
