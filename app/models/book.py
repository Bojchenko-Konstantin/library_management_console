from enum import Enum


class Status(Enum):
    IN_STOCK = "в наличии"
    GIVE_AWAY = "выдана"


class Book:
    """Book model"""

    def __init__(
        self,
        id: int,
        title: str,
        author: str,
        year: int,
        status: Status = Status.IN_STOCK,
    ) -> None:
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def convert_instance_to_dict(self) -> dict:
        """Convert instance of class 'Book' to dictionary for saving in JSON"""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status.value,
        }

    @staticmethod
    def create_object_from_dict(data: dict) -> "Book":
        """Create an instance of class 'Book' from dictionary"""
        return Book(
            data["id"],
            data["title"],
            data["author"],
            data["year"],
            Status(data["status"]),
        )
