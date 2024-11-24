import os
import json
import unittest

from typing import List, Dict
from models.book import Book
from models.library import Library


class TestLibrary(unittest.TestCase):
    def setUp(self) -> None:
        self.test_file = "test_library.json"
        self.library = Library(self.test_file)

    def tearDown(self) -> None:
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_book(self) -> None:
        self.library.add_book("О дивный новый мир", "Олдос Хаксли", 1932)
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "О дивный новый мир")

    def test_delete_book(self) -> None:
        self.library.add_book("О дивный новый мир", "Олдос Хаксли", 1932)
        self.library.delete_book(1)
        self.assertEqual(len(self.library.books), 0)

    def test_find_books_by_title(self) -> None:
        self.library.add_book("О дивный новый мир", "Олдос Хаксли", 1932)
        books: List[Book] = self.library.find_books("дивный", "название")
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].title, "О дивный новый мир")

    def test_find_books_by_author(self) -> None:
        self.library.add_book("О дивный новый мир", "Олдос Хаксли", 1932)
        books: List[Book] = self.library.find_books("Хаксли", "автор")
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].author, "Олдос Хаксли")

    def test_find_books_by_year(self) -> None:
        self.library.add_book("О дивный новый мир", "Олдос Хаксли", 1932)
        books: List[Book] = self.library.find_books("1932", "год")
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].year, 1932)

    def test_update_status(self) -> None:
        self.library.add_book("О дивный новый мир", "Олдос Хаксли", 1932)
        self.library.update_status(1, "выдана")
        self.assertEqual(self.library.books[0].status, "выдана")

    def test_save_books(self) -> None:
        self.library.add_book("О дивный новый мир", "Олдос Хаксли", 1932)
        self.library.save_books()
        with open(self.test_file, "r", encoding="utf-8") as file:
            data = json.load(file)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]["title"], "О дивный новый мир")

    def test_load_books(self) -> None:
        book_data: List[Dict[str, int | str]] = [
            {
                "id": 1,
                "title": "О дивный новый мир",
                "author": "Олдос Хаксли",
                "year": 1932,
                "status": "в наличии",
            }
        ]
        with open(self.test_file, "w", encoding="utf-8") as file:
            json.dump(book_data, file, ensure_ascii=False, indent=4)

        self.library.load_books()
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "О дивный новый мир")


if __name__ == "__main__":
    unittest.main()
