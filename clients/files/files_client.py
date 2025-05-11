from clients.api_clients import APIClient
from httpx import Response
from typing import TypedDict


class CreateFileRequestDict(TypedDict):
    """
    Тип данных для запроса на создание файла.
    """
    filename: str
    directory: str
    upload_file: str

class FilesClient(APIClient):
    """
    Клиент для работы с API файлов.
    """
    def __init__(self, client):
        super().__init__(client)
        self.base_url = "http://localhost:8000/api/v1/files"

    def get_files_api(self, file_id: str) -> Response:
        """
        Выполняет запрос на получение файла.

        :param file_id: ID файла.
        :return: Ответ от сервера.
        """
        return self.get(f"{self.base_url}/{file_id}")

    def create_file_api(self, request: CreateFileRequestDict) -> Response:
        """
        Выполняет запрос на добавления файла на сервер.

        :param request: Данные для добавления файла.
        :return: Ответ от сервера.
        """
        return self.post(
            f"{self.base_url}",
            data=request,
            files={"upload_file": open(request["upload_file"], "rb")}
        )

    def delete_file_api(self, file_id: str) -> Response:
        """
        Выполняет запрос на удаление файла.

        :param file_id: ID файла.
        :return: Ответ от сервера.
        """
        return self.delete(f"{self.base_url}/{file_id}")