import json
import uuid

import pytest

from libraries.error_handler import ErrorHandler
from ui.pages.charter_view_page import CharterViewPage
from ui.pages.home_page import HomePage
from ui.pages.login_page import LoginPage
from ui.pages.search_result_page import SearchResultsPage

from ui.utilities import browser


@pytest.mark.usefixtures("setup", "before_tests")
class TestMessageCaptain:

    @pytest.mark.end_to_end
    @ErrorHandler.error_handler
    def test_message_captain(self):
        """
        End-to-end test that check flow for sending inquiry to captain, for selected charter
        :param
        :return:
        """
        with open('../../test_data/test_home_page.json') as test_data:
            input_data = json.load(test_data)

        home_page = HomePage(browser.WEB_DRIVER, self.test_name)
        self.logger.log_info("Filling up search fields")
        home_page.fill_out_search_form(input_data)
        self.logger.log_info("Clicking on Check availability button")
        home_page.click_on_element(home_page.CHECK_AVAILABILITY_BUTTON)

        search_results_page = SearchResultsPage(browser.WEB_DRIVER, self.test_name)
        assert search_results_page.element_visible_condition(
            search_results_page.PAGE_INDICATOR), search_results_page.assert_msg("search page not reached")
        self.logger.log_info("Filtering results")
        search_results_page.click_on_element(search_results_page.FILTERS_BUTTON)
        search_results_page.element_visible_on_page(search_results_page.SHOW_CHARTERS_BUTTON)
        search_results_page.select_filters(input_data["filters"])
        search_results_page.click_on_element(search_results_page.SHOW_CHARTERS_BUTTON)
        search_results_page.loading_done(search_results_page.LOADER_ON_FILTERS)
        search_results_page.loading_done(search_results_page.LOADER_DOTS)
        self.logger.log_info("Selecting first Anglers choice")
        search_results_page.click_on_element(search_results_page.ANGLERS_CHOICE)
        browser.switch_to_latest_window()

        charter_view_page = CharterViewPage(browser.WEB_DRIVER, self.test_name)
        self.logger.log_info("Clicking on Message Captain button")
        charter_view_page.click_on_element(charter_view_page.MESSAGE_CAPTAIN_BUTTON)
        if charter_view_page.element_not_visible_on_page(charter_view_page.CREATE_NEW_INQUIRY):
            charter_view_page.click_on_element(charter_view_page.CREATE_NEW_INQUIRY)
        charter_view_page.element_visible_on_page(charter_view_page.MESSAGE_CAPTAIN_MODAL)
        home_page.default_wait(2)
        message_for_captain = uuid.uuid1().hex
        self.logger.log_info(f"Filling out message form with message: {message_for_captain}")
        charter_view_page.fill_out_captain_message_dialogue(message_for_captain)
        charter_view_page.click_on_element(charter_view_page.SEND_MESSAGE_BUTTON)
        self.logger.log_info("Sending message")
        assert charter_view_page.element_visible_condition(
            charter_view_page.MESSAGE_SENT_INFO), charter_view_page.assert_msg("Message Sent success info not shown")

    @pytest.fixture(scope='function')
    def before_tests(self, request):
        self.logger.log_info("Login")
        login_page = LoginPage(browser.WEB_DRIVER, self.test_name)
        login_page.login()
