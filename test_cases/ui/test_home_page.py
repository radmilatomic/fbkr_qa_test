import pytest
from libraries.error_handler import ErrorHandler

from ui.utilities import browser


@pytest.mark.usefixtures("setup")
class TestHomePage:

    @ErrorHandler.ui_error_handler
    def test_home_page(self):
        """
        TestDoc
        :param
        :return:
        """
        self.logger.log_info("Hello From FBKR test")
