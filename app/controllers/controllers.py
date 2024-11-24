from utils.constants import AVAILABLE_STATUSES
from models.library import Library
from utils.validate_prompts_and_value import (
    validate_value_id,
    validate_year_publication,
)


def delete_book_by_id(library: Library) -> None:
    book_id = validate_value_id("Введите ID книги для её удаления: ")
    library.delete_book(book_id)


def add_new_book(library: Library) -> None:
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    year = validate_year_publication("Введите год публикации: ")
    library.add_book(title, author, year)


def find_book(library: Library) -> None:
    while True:
        search_by = input("Искать по (название/автор/год): ").strip().lower()
        if search_by in ("название", "автор", "год"):
            break
        else:
            print("Ошибка: Пожалуйста, введите 'название', 'автор' или 'год'.")

    if search_by == "год":
        keyword = validate_year_publication("Введите год для поиска: ")
    elif search_by in ("название", "автор"):
        keyword = input("Введите ключевое слово для поиска: ")

    books = library.find_books(keyword, search_by)
    if books:
        for book in books:
            print(
                f"ID: {book.id}, Название: {book.title}, "
                f"Автор: {book.author}, Год: {book.year}, Статус: {book.status}"
            )
    else:
        print("Книги не найдены.")


def display_books(library: Library) -> None:
    library.show_all_books()


def update_status(library: Library):
    book_id = validate_value_id("Введите ID книги для изменения статуса: ")

    while True:
        new_status = input(f"Введите новый статус {AVAILABLE_STATUSES}: ").strip()
        if new_status in AVAILABLE_STATUSES:
            break
        print(
            f"Статус '{new_status}' отсутствует. Список доступных статусов: {AVAILABLE_STATUSES}"
        )
    library.update_status(book_id, new_status)
