import logging


class Logger:

    def __init__(self, name="FBKR_LOGGER", logging_level=logging.DEBUG,
                 log_format=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')):
        """
        :param name: name of the logger instance
        :param logging_level: level of logging
        :param log_format: formatting of the log
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging_level)

        # Logger handlers
        self.stdout_handler = logging.StreamHandler()
        self.stdout_handler.setLevel(logging_level)

        # Formatters for the handlers
        self.stdout_handler.setFormatter(log_format)

        # Add handlers to the logger
        self.logger.addHandler(self.stdout_handler)

    def log_set_up(self, method_name):
        self.logger.info("")
        self.logger.info("********************************************************************************************")
        self.logger.info("Setup for " + method_name)

    def log_tear_down(self, method_name):
        self.logger.info("********************************************************************************************")
        self.logger.info("tear down for " + method_name)
        self.logger.info("********************************************************************************************")

    def log_method_name(self, method_name):
        self.logger.info("********************************************************************************************")
        self.logger.info("EXECUTING TEST METHOD: " + method_name)
        self.logger.info("********************************************************************************************")
        self.logger.info("")

    def log_info(self, log_msg):
        self.logger.info("********************************************************************************************")
        self.logger.info(log_msg)

    def remove_handlers(self):
        self.logger.removeHandler(self.stdout_handler)

    def log_status_code(self, request_type, status_code):
        self.logger.info("********************************************************************************************")
        self.logger.info("Response status code after {0} request: {1}".format(request_type, status_code))

    def log_assert_message(self, message):
        self.logger.error(message)
        return message

    def status_code_assert(self, response_type, received, expected):
        message = "{0} request response status code not correct." \
            "Received: {1}, expected: {2}".format(response_type, received, expected)
        self.logger.info("********************************************************************************************")
        self.logger.error(message)
        return message

    def response_text_assert(self, received, expected):
        message = "Response text not correct. Received: {0}, expected: {1}".format(received, expected)
        self.logger.error(message)
        return message
