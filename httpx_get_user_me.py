from typing import Any
import httpx


def login(email: str, password: str) -> tuple[int, Any]:
    """
    Функция для выполнения входа в систему и получения токена доступа.
    :param email: Email пользователя.
    :param password: Пароль пользователя.
    :return: Вернет словарь с токенами доступа.
    """
    login_payload = {
        "email": email,
        "password": password
    }
    try:
        login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
        login_response.raise_for_status()
        return login_response.status_code, login_response.json()
    except httpx.HTTPStatusError as e:
        print(f"HTTP ошибка: {e.response.status_code} - {e.response.text}")
        exit(1)

def get_user_me(access_token: str) -> tuple[int, Any]:
    """
    Функция для получения информации о текущем пользователе.
    :param access_token: JWT токен доступа.
    :return: Вернет словарь с информацией о пользователе.
    """
    headers_with_token = {
        "Authorization": f"Bearer {access_token}"
    }
    try:
        user_me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers_with_token)
        user_me_response.raise_for_status()
        return user_me_response.status_code, user_me_response.json()
    except httpx.HTTPStatusError as e:
        print(f"HTTP ошибка: {e.response.status_code} - {e.response.text}")
        exit(1)



login_data = login("dopgor555@gmail.com", "123123g")
user_me_data = get_user_me(login_data[1].get("token").get("accessToken"))

print(login_data)
print(user_me_data)
