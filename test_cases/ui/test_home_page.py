import pytest

from libraries.error_handler import ErrorHandler
from ui.pages.home_page import HomePage
from ui.utilities import browser


@pytest.mark.usefixtures("setup")
class TestHomePage:

    @pytest.mark.component
    @ErrorHandler.error_handler
    def test_clear_search_input(self):
        """
        Component test that checks if clearing search input button is working
        :param
        :return:
        """
        search_keyword = "Florida"
        home_page = HomePage(browser.WEB_DRIVER, self.test_name)
        self.logger.log_info("Filling up search fields")
        home_page.fill_input_field(home_page.SEARCH_INPUT, search_keyword)
        assert home_page.element_visible_condition(home_page.SEARCH_FORM_SEARCH_RESULTS_DROPDOWN), home_page.assert_msg(
            f"Results are not shown when search keyword {search_keyword} is entered in search input")
        self.logger.log_info(
            f"Dropdown with search results is visible when search keyword {search_keyword} is entered in search input")
        home_page.click_on_element(home_page.SEARCH_FORM_INPUT_CLEAR_BUTTON)
        assert not home_page.element_visible_condition(
            home_page.SEARCH_FORM_SEARCH_RESULTS_DROPDOWN), home_page.assert_msg(
            "Results are not cleared after clearing search input field")
        self.logger.log_info("Results are cleared after clicking on clear search input field")
        search_input_text = home_page.find_element(home_page.SEARCH_INPUT).get_attribute("value")
        assert not search_input_text, home_page.assert_msg(
            "Search input field text is not cleared after clicking on clear search input button")
        self.logger.log_info("Search input field text is cleared after clicking on clear search input button.")
