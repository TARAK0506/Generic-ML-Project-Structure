import sys

def error_message_detail(error,error_detail:sys):
    """
    error_message_detail(error,error_detail)
    This function is used to print the error message and the error detail message.
    """
    file_name = exc_tb.tb_frame.f_code.co_filename
    _,_,exc_tb = error_detail.exc_info()     # Get the exception traceback on which file and line number the error occured.
    error_message = "Error occured in file: {0} at line number: {1} with error message: {2}".format(
       file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message

    class CustomException(Exception):
        def __init__(self, error_message,error_detail:sys):
            super().__init__(error_message)
            self.error_message = error_message_detail(error_message,error_detail = error_detail)

        def __str__(self):
            return self.error_message
        





