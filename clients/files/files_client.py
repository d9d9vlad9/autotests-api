import allure
from httpx import Response
from clients.api_clients import APIClient
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from clients.api_coverage import tracker
from tools.routes import APIRoutes


class FilesClient(APIClient):
    """
    Клиент для работы с API файлов. Методы: GET /api/v1/files, GET /api/v1/files/{fileId}, POST /api/v1/files, DELETE /api/v1/files/{fileId}.
    """
    @allure.step("Get file by id {file_id}")
    @tracker.track_coverage_httpx(f"{APIRoutes.FILES}/{{file_id}}")
    def get_file_api(self, file_id: str) -> Response:
        """
        Выполняет запрос на получение файла.

        :param file_id: ID файла.
        :return: Ответ от сервера.
        """
        return self.get(f"{APIRoutes.FILES}/{file_id}")

    @allure.step("Create file")
    @tracker.track_coverage_httpx(APIRoutes.FILES)
    def create_file_api(self, request: CreateFileRequestSchema) -> Response:
        """
        Выполняет запрос на добавления файла на сервер.

        :param request: Данные для добавления файла.
        :return: Ответ от сервера.
        """
        return self.post(
            APIRoutes.FILES,
            data=request.model_dump(by_alias=True, exclude={"upload_file"}),
            files={"upload_file": request.upload_file.read_bytes()}
        )

    @allure.step("Delete file by id {file_id}")
    @tracker.track_coverage_httpx(f"{APIRoutes.FILES}/{{file_id}}")
    def delete_file_api(self, file_id: str) -> Response:
        """
        Выполняет запрос на удаление файла.

        :param file_id: ID файла.
        :return: Ответ от сервера.
        """
        return self.delete(f"{APIRoutes.FILES}/{file_id}")


    def create_file(self, request: CreateFileRequestSchema) -> CreateFileResponseSchema:
        """
        Выполняет запрос на добавление файла и возвращает ID созданного файла.

        :param request: Данные для добавления файла.
        :return: ID созданного файла.
        """
        response = self.create_file_api(request)
        return CreateFileResponseSchema.model_validate_json(response.text)

def get_files_client(user: AuthenticationUserSchema) -> FilesClient:
    """
    Возвращает экземпляр клиента для работы с API файлов.

    :return: Экземпляр FilesClient.
    """
    return FilesClient(client=get_private_http_client(user))