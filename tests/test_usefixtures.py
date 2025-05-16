import pytest


@pytest.fixture
def clear_books_database():
    print("[FIXTURE] Удаление всех книг из базы данных")

@pytest.fixture
def fill_books_database():
    print("[FIXTURE] Заполнение базы данных книгами")

@pytest.mark.usefixtures("clear_books_database", "fill_books_database")
class TestLibrary:
    def tets_read_books_from_library(self):
        ...

    def test_delete_books_from_library(self):
        ...