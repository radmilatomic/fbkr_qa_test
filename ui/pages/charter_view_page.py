from selenium.webdriver.common.by import By

from ui.pages.base_page import BasePage


class CharterViewPage(BasePage):
    # Locators

    CONTACT_DATE_PICKER = (
        By.XPATH,
        "//div[input[@id='cf-trip-date']]",
        "date picker on contact captain form")

    CONTACT_TEXTAREA = (
        By.ID,
        "contact-textarea",
        "contact textarea")

    CREATE_NEW_INQUIRY = (
        By.XPATH,
        "//button[contains(text(),'Create new inquiry')]",
        "create new inquiry button")

    CURRENT_MONTH_DATE = (
        By.XPATH,
        "//td[contains(@class,'rdtDay') and not(contains(@class,'rdtOld')) and not(contains(@class,'rdtNew'))]",
        "date picker on contact captain form")

    GROUP_SIZE = (
        By.ID,
        "cf-group-size",
        "group size select")

    MESSAGE_CAPTAIN_BUTTON = (
        By.ID,
        "contact-captain",
        "message captain button")

    MESSAGE_CAPTAIN_MODAL = (
        By.XPATH,
        "//div[contains(@class,'modal-header')][h3[contains(text(),'Contact')]]",
        "message captain modal")

    MESSAGE_SENT_INFO = (
        By.XPATH,
        "//b[contains(text(),'Message Sent!')]",
        "message sent info")

    NEXT_MONTH_ARROW = (
        By.XPATH,
        "//th[contains(@class,'rdtNext')]",
        "next month arrow")

    SEND_MESSAGE_BUTTON = (
        By.XPATH,
        "//button[text()='Send Message']",
        "send message button")

    TRIPS_SELECT = (
        By.ID,
        "cf-packages",
        "trip select")

    TRIPS_SELECT_OPTIONS = (
        By.XPATH,
        "//select[@id='cf-packages']/option",
        "trip select options")

    # Locator methods

    def dropdown_option(self, option):
        locator = (
            By.XPATH,
            f"//option[contains(text(),'{option}')]",
            f"option {option}")
        return locator

    # Actions

    def fill_out_captain_message_dialogue(self, message):
        self.find_element(self.CONTACT_DATE_PICKER).click()
        last_current_date_element = self.find_elements(self.CURRENT_MONTH_DATE)[-1]
        element_classes = last_current_date_element.get_attribute('class')
        if "Disabled" in element_classes:
            self.click_on_element(self.NEXT_MONTH_ARROW)
            self.find_elements(self.CURRENT_MONTH_DATE)[-1].click()
        else:
            last_current_date_element.click()
        self.click_on_element(self.GROUP_SIZE)
        self.click_on_element(self.dropdown_option("2 persons"))
        self.click_on_element(self.TRIPS_SELECT_OPTIONS)
        self.find_elements(self.TRIPS_SELECT_OPTIONS)[-1].click()
        self.default_wait(2)
        self.fill_input_field(self.CONTACT_TEXTAREA, message)
