from utils.exceptions import CantReadPrompt, CantReadYearPublication


def validate_value_id(prompt: str) -> int:
    """Prompts the user to enter a number until it gets a valid value"""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            raise CantReadPrompt


def validate_year_publication(year: str) -> int:
    try:
        while True:
            value = int(input(year))
            if value > 0 and value < 2024:
                return value
    except ValueError:
        raise CantReadYearPublication
