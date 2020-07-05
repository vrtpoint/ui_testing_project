import logging
import os


def browser_log(logger_name):
    """Создание логгера для браузера"""

    try:
        os.stat('logs')
    except FileNotFoundError:
        os.mkdir('logs')

    log = logging.getLogger(logger_name)
    log.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    filehandler_info = logging.FileHandler(filename='logs/info.log', mode='a')
    filehandler_info.setLevel(level=logging.INFO)
    filehandler_info.setFormatter(formatter)

    filehandler_warning = logging.FileHandler(filename='logs/warning.log', mode='a')
    filehandler_warning.setLevel(level=logging.WARNING)
    filehandler_warning.setFormatter(formatter)

    filehandler_error = logging.FileHandler(filename='logs/error.log', mode='a')
    filehandler_error.setLevel(level=logging.ERROR)
    filehandler_error.setFormatter(formatter)

    log.addHandler(filehandler_info)
    log.addHandler(filehandler_warning)
    log.addHandler(filehandler_error)

    return log

