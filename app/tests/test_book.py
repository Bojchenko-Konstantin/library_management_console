import unittest

from typing import Dict
from models.book import Book


class TestBook(unittest.TestCase):
    """Tests for testing class Book"""

    def setUp(self) -> None:
        self.book = Book(1, "Снеговик", "Ю Несбё", 2007)

    def test_convert_instance_to_dict(self) -> None:
        expected: Dict[str, int | str] = {
            "id": 1,
            "title": "Снеговик",
            "author": "Ю Несбё",
            "year": 2007,
            "status": "в наличии",
        }
        self.assertEqual(self.book.convert_instance_to_dict(), expected)

    def test_create_object_from_dict(self) -> None:
        data: Dict[str, int | str] = {
            "id": 1,
            "title": "Снеговик",
            "author": "Ю Несбё",
            "year": 2007,
            "status": "в наличии",
        }
        book: Book = Book.create_object_from_dict(data)
        self.assertEqual(book.id, 1)
        self.assertEqual(book.title, "Снеговик")
        self.assertEqual(book.author, "Ю Несбё")
        self.assertEqual(book.year, 2007)
        self.assertEqual(book.status, "в наличии")


if __name__ == "__main__":
    unittest.main()
