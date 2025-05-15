import httpx
from tools.fakers import fake
from typing import Any
from httpx_get_user_me import login

def create_user() -> tuple[int, Any]:
    """
    Функция для создания нового пользователя.
    :return: Вернет словарь с информацией о созданном пользователе.
    """
    create_payload = {
        "email": fake.email(),
        "password": "string",
        "lastName": "string",
        "firstName": "string",
        "middleName": "string"
}
    try:
        create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_payload)
        create_user_response.raise_for_status()
        return create_user_response.status_code, create_user_response.json()
    except httpx.HTTPStatusError as e:
        print(f"HTTP ошибка: {e.response.status_code} - {e.response.text}")
        exit(1)

def update_user(user_id: str, access_token: str)-> tuple[int, Any]:
    """
    Функция для обновления информации о пользователе.
    :param user_id: ID пользователя.
    :param access_token: JWT токен доступа.
    :return: Вернет словарь с информацией об обновленном пользователе.
    """
    update_payload = {
        "email": get_random_email(),
        "lastName": "string",
        "firstName": "string",
        "middleName": "string"
}
    headers_with_token = {
        "Authorization": f"Bearer {access_token}"
    }
    try:
        update_user_response = httpx.patch(f"http://localhost:8000/api/v1/users/{user_id}", json=update_payload, headers=headers_with_token)
        update_user_response.raise_for_status()
        return update_user_response.status_code, update_user_response.json()
    except httpx.HTTPStatusError as e:
        print(f"HTTP ошибка: {e.response.status_code} - {e.response.text}")
        exit(1)


if __name__ == "__main__":
    user = create_user()[1].get("user")
    print(user)
    auth = login(user.get("email"), "string")
    print(auth)
    update = update_user(user.get("id"), auth[1].get("token").get("accessToken"))
    print(update)