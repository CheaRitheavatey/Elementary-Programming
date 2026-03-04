import logging
from datetime import datetime
from functools import wraps


logging.basicConfig(
    filename='file.txt',
    level=logging.INFO,
    format='%(message)s'
)

def log_decorator(func):
    """decorator"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        log_message = f"Function '{func.__name__}' called from module '{func.__module__}' at {datetime.now()}"
        logging.info(log_message)
        
        print(log_message)
        
        return func(*args, **kwargs)
    return wrapper


@log_decorator
def a():
    print("Hello!")

a()