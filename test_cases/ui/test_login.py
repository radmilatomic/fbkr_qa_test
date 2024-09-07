import pytest

from libraries.error_handler import ErrorHandler
from test_data.data_login import positive_login_data, negative_login_data
from ui.pages.login_page import LoginPage
from ui.utilities import browser


@pytest.mark.usefixtures("setup")
class TestLogin:
    login_params_positive = positive_login_data
    login_params_negative = negative_login_data

    @pytest.mark.end_to_end
    @pytest.mark.parametrize("username,password", login_params_positive)
    def test_login_positive(self, username, password):
        """
        End-to-end test that checks if user can successfully log into Fishing Booker site
        :param
        :return:
        """

        @ErrorHandler.error_handler
        def login_positive_method():
            login_page = LoginPage(browser.WEB_DRIVER, self.test_name)
            login_page.login(username, password)
            self.logger.log_info("Filling up login form.")
            assert login_page.element_visible_condition(login_page.NAVIGATION_USERNAME_BUTTON), login_page.assert_msg(
                "Button with username not visible in navigation.")
            self.logger.log_info("Successful login. Button with username visible in navigation.")

        login_positive_method()

    @pytest.mark.end_to_end
    @pytest.mark.parametrize("username,password", login_params_negative)
    def test_login_negative(self, username, password):
        """
        End-to-end test that checks if user can successfully log into Fishing Booker site
        :param
        :return:
        """

        @ErrorHandler.error_handler
        def login_negative_method():
            login_page = LoginPage(browser.WEB_DRIVER, self.test_name)
            login_page.login(username, password)
            self.logger.log_info("Filling up login form")
            assert login_page.element_visible_condition(login_page.LOGIN_ERROR), login_page.assert_msg(
                "Error message with wrong username/password info not visible on the screen.")
            assert not login_page.element_visible_condition(
                login_page.NAVIGATION_USERNAME_BUTTON), login_page.assert_msg(
                "Button with username visible in navigation.")
            self.logger.log_info(
                "User is not able to login with incorrect data. Proper message is shown. Button with username is not visible in navigation.")

        login_negative_method()
