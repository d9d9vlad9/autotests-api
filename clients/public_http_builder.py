from httpx import Client

def get_public_http_client() -> Client:
    """
    Создает и возвращает экземпляр httpx.Client с настройками для публичного HTTP-клиента.
    :return: Экземпляр httpx.Client.
    """
    return Client(timeout=5, base_url="http://localhost:8000")