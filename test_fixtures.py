import pytest


@pytest.fixture
def user_client():
    print("Creating a user client")


class TestUserFlow:
    def test_user_can_login(self, user_client):
        ...

    def test_user_can_create_course(self, user_client):
        ...