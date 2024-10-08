from selenium.webdriver.common.by import By

from ui.pages.base_page import BasePage


class HomePage(BasePage):
    # Locators

    ADD_ADULTS_BUTTON = (
        By.ID,
        "adults-plus",
        "add adults button")

    ADD_CHILDREN_BUTTON = (
        By.ID,
        "children-plus",
        "add children button")

    AVAILABLE_DATE = (
        By.XPATH,
        "//button[contains(@class,'rdp-button') and not (contains(@class,'rdp-day_disabled'))]",
        "first available date")

    CHECK_AVAILABILITY_BUTTON = (
        By.XPATH,
        "//div[a[@data-testid='search-form-check-availability-button']]",
        "check availabilty button on home page")

    GROUP_SIZE_INPUT = (
        By.ID,
        "group-size-picker-input",
        "group-size-picker-input")

    DATE_PICKER_INPUT = (
        By.ID,
        "date-picker",
        "date picker input")

    NUMBER_OF_PRESELECTED_ADULTS = (
        By.XPATH,
        "//button[@id='adults-minus']/following-sibling::div/strong",
        "number of preselected adults")

    NUMBER_OF_PRESELECTED_CHILDREN = (
        By.XPATH,
        "//button[@id='children-minus']/following-sibling::div/strong",
        "number of preselected adults")

    REMOVE_ADULTS_BUTTON = (
        By.ID,
        "adults-minus",
        "remove adults button")

    REMOVE_CHILDREN_BUTTON = (
        By.ID,
        "children-minus",
        "remove children button")

    SEARCH_FORM_INPUT_CLEAR_BUTTON = (
        By.XPATH,
        "//span[@data-testid='search-form-input-clear-button']",
        "Clear search from input button")

    SEARCH_FORM_SEARCH_RESULTS_DROPDOWN = (
        By.XPATH,
        "//div[@data-testid='search-form-search-results-dropdown']",
        "Destination Search results dropdown")

    SEARCH_INPUT = (
        By.XPATH,
        "//input[@data-testid='search-form-input-field']",
        "search button on home page")

    SEARCH_SUGGESTION = (
        By.XPATH,
        "//div[contains(@data-testid,'search-form-suggestion')]/span",
        "search button on home page")


    # Locator methods

    def search_dropdown_option(self, entered_keyword):
        locator = (
            By.XPATH,
            "//span[text()='{0}']".format(entered_keyword),
            "dropdown option {0}".format(entered_keyword))
        return locator

    # Actions

    def select_group(self, group_data):
        number_of_preselected_adults = int(self.find_element(self.NUMBER_OF_PRESELECTED_ADULTS).text)
        number_of_preselected_children = int(self.find_element(self.NUMBER_OF_PRESELECTED_CHILDREN).text)
        if group_data[0] - number_of_preselected_adults < 0:
            for iteration in range(number_of_preselected_adults - group_data[0]):
                self.click_on_element(self.REMOVE_ADULTS_BUTTON)
        elif group_data[0] - number_of_preselected_adults > 0:
            for iteration in range(group_data[0] - number_of_preselected_adults):
                self.click_on_element(self.ADD_ADULTS_BUTTON)

        if group_data[1] - number_of_preselected_children < 0:
            for iteration in range(number_of_preselected_children - group_data[1]):
                self.click_on_element(self.REMOVE_CHILDREN_BUTTON)
        elif group_data[1] - number_of_preselected_adults > 0:
            for iteration in range(group_data[1] - number_of_preselected_children):
                self.click_on_element(self.ADD_CHILDREN_BUTTON)

    def fill_out_search_form(self, input_data):
        self.fill_input_field(self.SEARCH_INPUT, input_data["destination"])
        self.find_elements(self.search_dropdown_option(input_data["destination"]))[0].click()
        self.click_on_element(self.DATE_PICKER_INPUT)
        available_date_class = self.find_element(self.AVAILABLE_DATE).get_attribute('class')
        if 'selected' not in available_date_class:
            self.click_on_element(self.AVAILABLE_DATE)
        self.click_on_element(self.GROUP_SIZE_INPUT)
        self.select_group(input_data["group"])
