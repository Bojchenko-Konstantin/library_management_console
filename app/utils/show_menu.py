from .constants import MENU_OPTIONS


def show_menu_options() -> None:
    """Отображает список команд библиотеки."""
    print("\nСписок команд библиотеки:")
    for key, value in MENU_OPTIONS.items():
        print(f"{key}. {value}")
    print("\n")
