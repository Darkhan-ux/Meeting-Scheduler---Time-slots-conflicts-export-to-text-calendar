import re
from datetime import datetime


def validate_name(name):
    return len(name.strip()) >= 2


def validate_email(email):
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    return re.fullmatch(pattern, email.strip()) is not None


def validate_date(date_text):
    """Validate real calendar date in YYYY-MM-DD format."""
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", date_text.strip()) is None:
        return False

    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def validate_time(time_text):
    pattern = r"([01][0-9]|2[0-3]):[0-5][0-9]"
    return re.fullmatch(pattern, time_text.strip()) is not None
