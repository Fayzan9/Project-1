import logging
import os
from logging.handlers import RotatingFileHandler

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()

LOG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)


def setup_logging():
    logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)

    logger = logging.getLogger()

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter(LOG_FORMAT))
    logger.addHandler(console_handler)

    # Rotating File Handler
    file_handler = RotatingFileHandler(
        f"{LOG_DIR}/app.log",
        maxBytes=5 * 1024 * 1024,  # 5MB
        backupCount=3
    )
    file_handler.setFormatter(logging.Formatter(LOG_FORMAT))
    logger.addHandler(file_handler)