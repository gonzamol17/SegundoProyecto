import inspect
from Utils.logger_manager import get_logger

class BaseClass:
    def get_Logger(self):
        caller_name = inspect.stack()[1][3]
        return get_logger(caller_name)