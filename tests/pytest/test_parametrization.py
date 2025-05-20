import pytest
from _pytest.fixtures import SubRequest

@pytest.mark.parametrize("number", [1, 2, 3, -1])
def test_number(number: int):
    assert number > 0

@pytest.mark.parametrize(
    "number, expected",
    [(1, 1), (2, 4), (3, 9), (-1, 1)]
)
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected

@pytest.mark.parametrize(
    "os",
    ["linux", "windows", "mac"])
@pytest.mark.parametrize(
    "host",
    ["localhost", "dev.example.com", "prod.example.com"]
)
def test_os_hostname(os, host):
    assert len(os + host) > 0

@pytest.fixture(params=[
    "http://localhost",
    "http://dev.example.com",
    "http://prod.example.com"
])
def host(request: SubRequest):
    return request.param

def test_host(host):
    print(f"Host: {host}")

@pytest.mark.parametrize(
    'a, b, expected',
    [(1, 2, 3),
     (2, 3, 5),
     (3, 4, 7),
     (4, 5, 9),
     (5, 6, 11)]
)
class TestOperations:
    def test_addition(self, a: int, b: int, expected: int):
        assert a + b == expected

users = {
    "+70000000011": "User with money on bank account",
    "+70000000022": "User without money on bank account",
    "+70000000033": "User with operations on bank account"
}

@pytest.mark.parametrize(
    "phone_number",
    users.keys(),  # Передаем список номеров телефонов
    ids=lambda phone_number: f"{phone_number}: {users[phone_number]}"  # Генерируем идентификаторы динамически
)
def test_identifiers(phone_number: str):
    pass