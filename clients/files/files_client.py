from clients.api_clients import APIClient
from httpx import Response
from typing import TypedDict
from clients.private_http_builder import get_private_http_client, AuthenticationUserDict


class File(TypedDict):
    """
    Тип данных для файла.
    """
    id: str
    url: str
    filename: str
    directory: str

class CreateFileRequestDict(TypedDict):
    """
    Тип данных для запроса на создание файла.
    """
    filename: str
    directory: str
    upload_file: str

class CreateFileResponseDict(TypedDict):
    """
    Тип данных для ответа на запрос создания файла.
    """
    file: File

class FilesClient(APIClient):
    """
    Клиент для работы с API файлов. Методы: GET /api/v1/files, GET /api/v1/files/{fileId}, POST /api/v1/files, DELETE /api/v1/files/{fileId}.
    """
    def get_files_api(self, file_id: str) -> Response:
        """
        Выполняет запрос на получение файла.

        :param file_id: ID файла.
        :return: Ответ от сервера.
        """
        return self.get(f"/api/v1/files/{file_id}")

    def create_file_api(self, request: CreateFileRequestDict) -> Response:
        """
        Выполняет запрос на добавления файла на сервер.

        :param request: Данные для добавления файла.
        :return: Ответ от сервера.
        """
        return self.post(
            "/api/v1/files",
            data=request,
            files={"upload_file": open(request["upload_file"], "rb")}
        )

    def delete_file_api(self, file_id: str) -> Response:
        """
        Выполняет запрос на удаление файла.

        :param file_id: ID файла.
        :return: Ответ от сервера.
        """
        return self.delete(f"/api/v1/files/{file_id}")

    def create_file(self, request: CreateFileRequestDict) -> CreateFileResponseDict:
        """
        Выполняет запрос на добавление файла и возвращает ID созданного файла.

        :param request: Данные для добавления файла.
        :return: ID созданного файла.
        """
        response = self.create_file_api(request)
        return response.json()

def get_files_client(user: AuthenticationUserDict) -> FilesClient:
    """
    Возвращает экземпляр клиента для работы с API файлов.

    :return: Экземпляр FilesClient.
    """
    return FilesClient(client=get_private_http_client(user))