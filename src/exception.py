import sys
from logger import logger  # Import the configured logger from the logger module

def error_message_detail(error, error_detail: sys):
    # Extracting the traceback object from the error detail.
    # 'error_detail' is expected to be a tuple containing exception type, value, and traceback.
    _, _, exc_tb = error_detail

    # Retrieving the file name and line number where the error occurred.
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Formatting the error message with the script name, line number, and error message.
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))

    return error_message

class CustomException(Exception):
    # Custom exception class for more detailed error handling.
    def __init__(self, error_message, error_detail):
        # Initializing the base Exception class with the error message.
        super().__init__(error_message)

        # Storing a detailed error message, including file and line number of the error.
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        # Overriding the string representation of the exception to return the detailed error message.
        return self.error_message
    
# The following commented-out code demonstrates how to use the CustomException in an application.
# Uncomment to use in a script where you need detailed error handling.

# if __name__ == "__main__":
#     try:
#         # Example code that might raise an exception.
#         a = 1 / 0
#     except Exception as e:
#         # Capturing the exception details.
#         exc_type, exc_value, exc_tb = sys.exc_info()

#         # Logging the error using the imported logger.
#         logger.info("Divide by Zero") 

#         # Raising the custom exception with the original error and detailed information.
#         raise CustomException(e, (exc_type, exc_value, exc_tb))
