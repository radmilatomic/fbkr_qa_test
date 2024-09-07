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

    def log_assert_message(self, message):
        self.logger.error(message)
        return message
