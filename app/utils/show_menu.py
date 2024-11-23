from models.enums import MenuOptions


def show_menu_options() -> None:
    """Show list commands library"""
    print("\nСписок команд библиотеки:")
    for option in MenuOptions:
        print(f"{option.value}")
    print("\n")
