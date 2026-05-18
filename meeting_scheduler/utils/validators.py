import re


def validate_name(name):
    return len(name.strip()) >= 2


def validate_email(email):
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    return re.fullmatch(pattern, email) is not None


def validate_date(date_text):
    pattern = r"\d{4}-\d{2}-\d{2}"
    return re.fullmatch(pattern, date_text) is not None


def validate_time(time_text):
    pattern = r"([01][0-9]|2[0-3]):[0-5][0-9]"
    return re.fullmatch(pattern, time_text) is not None
