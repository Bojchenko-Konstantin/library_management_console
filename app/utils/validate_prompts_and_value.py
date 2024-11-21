from app.utils.exceptions import CantReadPrompt, CantReadYearPublication


def validate_value_id(prompt: int) -> int:
    """Prompts the user to enter a number until it gets a valid value"""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            raise CantReadPrompt


def validate_year_publication(year: int) -> int:
    try:
        while True:
            value = int(input(year))
            if year > 0 and year < 2024:
                return value
    except ValueError:
        raise CantReadYearPublication
