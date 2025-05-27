from httpx import Client
from clients.event_hooks import curl_event_hook


def get_public_http_client() -> Client:
    """
    Создает и возвращает экземпляр httpx.Client с настройками для публичного HTTP-клиента.
    :return: Экземпляр httpx.Client.
    """
    return Client(
        timeout=5,
        base_url="http://localhost:8000",
        event_hooks={"request": [curl_event_hook]},
    )