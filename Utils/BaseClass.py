import inspect
import logging
import os

from Utils.logger_manager import get_logger

class BaseClass:
    def get_Logger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Logs", "logfile.log")
        os.makedirs(os.path.dirname(log_path), exist_ok=True)
        fileHandler = logging.FileHandler(log_path, encoding="utf-8")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger