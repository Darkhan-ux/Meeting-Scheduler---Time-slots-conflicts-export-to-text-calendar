from functools import wraps


def log_action(func):
    """Simple decorator for showing which scheduler action was called."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Action: {func.__name__}")
        return func(*args, **kwargs)

    return wrapper
