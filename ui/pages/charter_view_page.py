from selenium.webdriver.common.by import By

from ui.pages.base_page import BasePage


class CharterViewPage(BasePage):
    # Locators
    MESSAGE_CAPTAIN_BUTTON = (
        By.ID,
        "contact-captain",
        "message captain button")

    CONTACT_DATE_PICKER = (
        By.ID,
        "cf-trip-date",
        "date picker on contact captain form")

    CURRENT_MONTH_DATE = (
        By.XPATH,
        "//td[contains(@class,'rdtDay') and not (contains(@class,'rdtOld')) and not (contains(@class,'rdtNew'))]",
        "date picker on contact captain form")

    NEXT_MONTH_ARROW = (
        By.XPATH,
        "//th[contains(@class,'rdtNext')]",
        "next month arrow")



    def filter_option(self, option):
        locator = (
            By.XPATH,
            f"//label[input[@name='{option}']]",
            f"filter option {option}")
        return locator

    def select_filters(self,filter_array):
        for filter_array_item in filter_array:
            self.click_on_element(self.filter_option(filter_array_item))







