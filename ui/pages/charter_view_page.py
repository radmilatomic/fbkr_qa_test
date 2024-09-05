from selenium.webdriver.common.by import By

from ui.pages.base_page import BasePage


class CharterViewPage(BasePage):
    # Locators
    MESSAGE_CAPTAIN_BUTTON = (
        By.ID,
        "contact-captain",
        "message captain button")

    MESSAGE_CAPTAIN_MODAL = (
        By.XPATH,
        "//div[contains(@class,'modal-header')][h3[contains(text(),'Contact')]]",
        "message captain modal")

    CREATE_NEW_INQUIRY = (
        By.XPATH,
        "//button[contains(text(),'Create new inquiry')]",
        "create new inquiry button")

    CONTACT_DATE_PICKER = (
        By.XPATH,
        "//div[input[@id='cf-trip-date']]",
        "date picker on contact captain form")

    CURRENT_MONTH_DATE = (
        By.XPATH,
        "//td[contains(@class,'rdtDay') and not(contains(@class,'rdtOld')) and not(contains(@class,'rdtNew'))]",
        "date picker on contact captain form")

    NEXT_MONTH_ARROW = (
        By.XPATH,
        "//th[contains(@class,'rdtNext')]",
        "next month arrow")

    GROUP_SIZE = (
        By.ID,
        "cf-group-size",
        "group size select")

    GROUP_SIZE_OPTION = (
        By.XPATH,
        "//option[contains(text(),'2 persons')]",
        "2 person group size")

    TRIPS_SELECT = (
        By.ID,
        "cf-packages",
        "trip select")

    TRIPS_SELECT_OPTION = (
        By.XPATH,
        "//select[@id='cf-packages']/option",
        "trip select options")

    CONTACT_TEXTAREA = (
        By.ID,
        "contact-textarea",
        "contact textarea")

    SEND_MESSAGE_BUTTON = (
        By.XPATH,
        "//button[text()='Send Message']",
        "send message button")

    MESSAGE_SENT_INFO = (
        By.XPATH,
        "//b[contains(text(),'Message Sent!')]",
        "message sent info")

    # //button[text()='Send Message']

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
        self.click_on_element(self.GROUP_SIZE_OPTION)

        self.click_on_element(self.TRIPS_SELECT_OPTION)
        self.find_elements(self.TRIPS_SELECT_OPTION)[-1].click()
        self.default_wait(2)
        self.fill_input_field(self.CONTACT_TEXTAREA, message)
