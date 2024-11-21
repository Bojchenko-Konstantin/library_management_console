import os
import json

from typing import List

from .book import Book, Status


class Library:
    """Library model"""

    def __init__(self, data_file: str):
        self.data_file = data_file or os.path.join(
            os.path.dirname(__file__), "..", "library.json"
        )
        self.books: List[Book] = []
        self._init_library()

    def _init_library(self) -> None:
        """Initializes the library by checking for the presence of the file and loading books"""
        if not os.path.exists(self.data_file):
            self._create_empty_library_file()
        self.load_books()

    def _create_empty_library_file(self) -> None:
        """Create an empty library JSON file"""
        with open(self.data_file, "w", encoding="utf-8") as file:
            json.dump([], file, ensure_ascii=False, indent=4)

    def load_books(self) -> None:
        """load books from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r", encoding="utf-8") as file:
                    books_data = json.load(file)
                    self.books = [
                        Book.create_object_from_dict(book) for book in books_data
                    ]
            except json.JSONDecodeError:
                print(
                    "Ошибка чтения данных: файл повреждён или содержит недопустимый JSON."
                )
                self.books = []
            except Exception as e:
                print(f"Ошибка при загрузке данных - {e}")
                self.books = []

    def save_books(self) -> None:
        """Save books in JSON"""
        with open(self.data_file, "w", encoding="utf-8") as file:
            json.dump(
                [book.convert_instance_to_dict() for book in self.books],
                file,
                ensure_ascii=False,
                indent=4,
            )

    def find_books(self, keyword: str, search_by: str) -> List[Book]:
        match search_by:
            case "название":
                return [
                    book for book in self.books if keyword.lower() in book.title.lower()
                ]
            case "автор":
                return [
                    book
                    for book in self.books
                    if keyword.lower() in book.author.lower()
                ]
            case "год":
                return [book for book in self.books if str(book.year) == keyword]
            case _:
                return []

    def add_book(self, title: str, author: str, year: int) -> None:
        """Add new book in library"""
        new_id = max([book.id for book in self.books], default=0) + 1
        new_book = Book(new_id, title, author, year)
        self.books.append(new_book)
        self.save_books()

    def delete_book_by_id(self, book_id: int) -> None:
        """Delete book from library by ID"""
        book_to_delete = next((book for book in self.books if book.id == book_id), None)
        if book_to_delete:
            self.books.remove(book_to_delete)
            self.save_books()
        else:
            print(f"В библиотеке книга с ID {book_id} отсутствует.")

    def show_all_books(self) -> None:
        """Show all books in library"""
        if self.books:
            for book in self.books:
                print(
                    f"ID: {book.id},\n"
                    f"Название книги: {book.title},\n"
                    f"Автор: {book.author},\n"
                    f"Год: {book.year},\n"
                    f"Статус: {book.status.value}"
                )
        else:
            print("В библиотеке книги отсутствуют")

    def update_status_by_ID(self, book_id: int, new_status: str) -> None:
        """Update status by ID"""
        book_to_update = next((book for book in self.books if book.id == book_id), None)
        if book_to_update:
            if isinstance(new_status, Status):
                book_to_update.status = new_status
                self.save_books()
            else:
                print(
                    f"Неправильный статус. Доступные статусы: {[status.value for status in Status]}."
                )
        else:
            print(f"Книга с ID {book_id} в библиотеке не найдена.")
