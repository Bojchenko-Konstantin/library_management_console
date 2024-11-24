from models.library import Library
from utils.show_menu import show_menu_options
from controllers.controllers import (
    add_new_book,
    delete_book_by_id,
    find_book,
    display_books,
    update_status,
)


def get_choice_from_menu() -> None:
    library = Library()

    try:
        while True:
            show_menu_options()

            choice = input("Выберите номер действия : ")

            if choice == "1":
                add_new_book(library)

            elif choice == "2":
                delete_book_by_id(library)

            elif choice == "3":
                find_book(library)

            elif choice == "4":
                display_books(library)

            elif choice == "5":
                update_status(library)

            elif choice == "6":
                break
            else:
                print("Неправильный выбор. Попробуйте снова.")

            if input("\nПродолжить работу (да/нет): ") == "нет":
                break
    except KeyboardInterrupt:
        print("\nЗавершение работы.")
