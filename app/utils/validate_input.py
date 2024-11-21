from app.utils.exceptions import CantReadPrompt


def validate_input(prompt: int) -> int:
    """Prompts the user to enter a number until it gets a valid value"""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            raise CantReadPrompt
