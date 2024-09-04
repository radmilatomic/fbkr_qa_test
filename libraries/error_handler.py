import logging
import traceback
from functools import wraps



class ErrorHandler:

    @classmethod
    def ui_error_handler(cls, func):
        """
        Decorator for error handling during the UI tests.
        Return the exception and take a screenshot on problematic screen.
        :param func: function to handle exception and take screenshots
        :return: if error occurs function with handled exceptions else input function
        """

        def new_func(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                error = e
                logging.getLogger('FBKR_LOGGER').error(f'An error occurred: {error}')
                logging.getLogger('XBOT_LOGGER').error(f'Error traceback: {traceback.format_exc()}')
            assert False, error

        return new_func