from selenium.webdriver.common.by import By

from ui.pages.base_page import BasePage


class SearchResultsPage(BasePage):
    # Locators
    PAGE_INDICATOR = (
        By.XPATH,
        "//li[contains(text(),'Search Results')]",
        "search results page indicator")

    FILTERS_BUTTON = (
        By.ID,
        "search-results-modal-btn-container",
        "filters button results page")

    ANGLERS_CHOICE = (
        By.XPATH,
        "//div[div[contains(@class,'listing-card-anglers-choice-header')]]/following-sibling::div",
        "first anglers choice option")

    REVIEW_SCORE = (
        By.XPATH,
        "//label[input[@name='4_50']]",
        "review_score_4.5")

    INSHORE_FISHING = (
        By.XPATH,
        "//label[input[@name='fishing_type_inshore']]",
        "inshore fishing")

    RED_SNAPPER = (
        By.XPATH,
        "//label[input[@name='snapper_red']]",
        "red snapper")

    SHOW_CHARTERS_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Show') and contains(text(),'charters')]",
        "show charters button")

    LOADER_ON_FILTERS = (
        By.XPATH,
        "//div[contains(@class,'lds-spin')]",
        "loader")

    def filter_option(self, option):
        locator = (
            By.XPATH,
            f"//label[input[@name='{option}']]",
            f"filter option {option}")
        return locator

    def select_filters(self,filter_array):
        for filter_array_item in filter_array:
            self.click_on_element(self.filter_option(filter_array_item))







