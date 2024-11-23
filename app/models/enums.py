from enum import Enum


class Status(Enum):
    IN_STOCK = "в наличии"
    GIVE_AWAY = "выдана"


class MenuOptions(Enum):
    ADD_BOOK = "Добавить книгу"
    DELETE_BOOK = "Удалить книгу"
    FIND_BOOK = "Найти книгу"
    SHOW_ALL_BOOKS = "Показать все книги"
    CHANGE_STATUS = "Изменить статус книги"
    EXIT = "Выход"
