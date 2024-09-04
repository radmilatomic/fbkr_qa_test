import json

import pytest
from libraries.error_handler import ErrorHandler
from ui.pages.charter_view_page import CharterViewPage
from ui.pages.home_page import HomePage
from ui.pages.login_page import LoginPage
from ui.pages.search_result_page import SearchResultsPage

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
        with open('../../test_data/test_home_page.json') as test_data:
            input_data = json.load(test_data)
        self.logger.log_info("Hello From FBKR test")

        home_page = HomePage(browser.WEB_DRIVER)
        login_page=LoginPage(browser.WEB_DRIVER)
        login_page.login()
        home_page.default_wait(2)
        # browser.open_url('https://qahiringtask.dev.fishingbooker.com')

        home_page.fill_input_field(home_page.SEARCH_INPUT, input_data["destination"])
        home_page.default_wait(2)
        home_page.find_elements(home_page.search_dropdown_option(input_data["destination"]))[0].click()
        home_page.default_wait(3)
        home_page.click_on_element(home_page.DATE_PICKER_INPUT)
        home_page.default_wait(3)
        home_page.click_on_element(home_page.AVAILABLE_DATE)
        home_page.default_wait(2)
        home_page.click_on_element(home_page.GROUP_SIZE_INPUT)
        home_page.default_wait(2)
        home_page.select_group(input_data["group"])
        home_page.default_wait(3)
        home_page.click_on_element(home_page.CHECK_AVAILABILITY_BUTTON)
        home_page.default_wait(3)
        search_results_page = SearchResultsPage(browser.WEB_DRIVER)
        assert search_results_page.element_visible_condition(
            search_results_page.PAGE_INDICATOR), "search page not reached"
        search_results_page.click_on_element(search_results_page.FILTERS_BUTTON)
        search_results_page.default_wait(3)
        search_results_page.element_visible_on_page(search_results_page.SHOW_CHARTERS_BUTTON)
        search_results_page.select_filters(input_data["filters"])
        search_results_page.default_wait(2)
        search_results_page.click_on_element(search_results_page.SHOW_CHARTERS_BUTTON)
        search_results_page.loading_done(search_results_page.LOADER_ON_FILTERS)
        search_results_page.default_wait(2)
        search_results_page.click_on_element(search_results_page.ANGLERS_CHOICE)
        search_results_page.default_wait(2)
        charter_view_page=CharterViewPage(browser.WEB_DRIVER)
        browser.switch_to_latest_window()
        charter_view_page.click_on_element(charter_view_page.MESSAGE_CAPTAIN_BUTTON)
        search_results_page.default_wait(2)
        charter_view_page.click_on_element(charter_view_page.CONTACT_DATE_PICKER)
        search_results_page.default_wait(2)
        last_current_date_element=charter_view_page.find_elements(charter_view_page.CURRENT_MONTH_DATE)[-1]
        element_classes=last_current_date_element.get_attribute('class')
        print(element_classes)
        if "Disabled" in element_classes:
            charter_view_page.click_on_element(charter_view_page.NEXT_MONTH_ARROW)
            charter_view_page.find_elements(charter_view_page.CURRENT_MONTH_DATE)[-1].click()
        else:
            last_current_date_element.click()

        search_results_page.default_wait(10)
        #
        # # browser.open_url(
        # #     'https://qahiringtask.dev.fishingbooker.com/charters/search/us/FL?search_location=&booking_date=09-03-2024&booking_days=1&booking_persons=6&booking_children=2&orderby=recommended&offset=0&limit=10&reviewScoreFilter%5B%5D=4_50&fishingTypeFilter%5B%5D=fishing_type_inshore&fishFilter%5B%5D=snapper_red')
        # # search_results_page.default_wait(10)
