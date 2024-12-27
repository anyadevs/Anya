import logging
from logging.handlers import RotatingFileHandler

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(console_formatter)
    file_handler = RotatingFileHandler("logs/app.log", maxBytes=5 * 1024 * 1024, backupCount=3)
    file_formatter = logging.Formatter("%(asctime)s - %(message)s")
    file_handler.setFormatter(file_formatter)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger
