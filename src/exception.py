import sys
from src.logging import get_logger

class RL_Exception(Exception):
    " Exception Configuration "
    def __init__(self,message=None,errors=None):
        super().__init__(message)
        self,errors=errors
        if message:
            " Log the Error Message "
            logging.error(message)
        if errors:
            " Log the Error Details "
            logging.error(errors)

class CustomException(RL_Exception):
    "Exception Raised"
    def __init__(self,message="Error Raised", errors=None):
        super().__init__(message,errors)
