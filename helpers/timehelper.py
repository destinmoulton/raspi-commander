from datetime import datetime
from config import TIME_FORMAT


def get_now_formatted():
    # Get the time
    return datetime.now().strftime(TIME_FORMAT)
