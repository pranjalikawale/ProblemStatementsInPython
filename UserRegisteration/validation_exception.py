#from validation_enum import ValidationEnum
#from enum import Enum

class ValidationException(Exception):
    def __init__(self, message, type):
        super().__init__(message)
        self.type=type