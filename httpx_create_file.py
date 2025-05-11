from httpx_update_user import create_user
from httpx_get_user_me import login
import httpx
from typing import Any

def add_file_to_user(user_id: str, access_token: str) -> tuple[int, Any]:
    """
    Функция для добавления файла к пользователю.
    :param user_id: ID пользователя.
    :param access_token: JWT токен доступа.
    """
    headers_with_token = {
        "Authorization": f"Bearer {access_token}"
    }
    create_user_response = {
        "upload_file": open('./testdata/files/image.png', 'rb')
    }
    try:
        create_file_response = httpx.post(
            f"http://localhost:8000/api/v1/files",
            data={"filename": "image.png","directory": "courses"},
            headers=headers_with_token,
            files=create_user_response)
        create_file_response.raise_for_status()
        print("Файл успешно добавлен")
        return create_file_response.status_code, create_file_response.json()
    except httpx.HTTPStatusError as e:
        print(f"HTTP ошибка: {e.response.status_code} - {e.response.text}")
        exit(1)

if __name__ == "__main__":
    user = create_user()[1].get("user")
    print(user)
    auth = login(user.get("email"), "string")
    print(auth)
    add_file_to_user(user.get("id"), auth[1].get("token").get("accessToken"))