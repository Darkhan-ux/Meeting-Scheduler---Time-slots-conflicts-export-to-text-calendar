def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Action: {func.__name__}")
        return func(*args, **kwargs)

    return wrapper
