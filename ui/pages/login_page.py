from selenium.webdriver.common.by import By

from libraries.properties import get_property
from ui.pages.base_page import BasePage


class LoginPage(BasePage):
    # Locators

    CONTINUE_WITH_EMAIL_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Continue with email')]",
        "Continue with email button")

    EMAIL_INPUT = (
        By.XPATH,
        "//input[@name='email']",
        "email input")

    LOGIN_BUTTON_FOR_DIALOGUE = (
        By.XPATH,
        "//p[contains(text(),'Log in')]",
        "Login button to open login dialogue")

    LOGIN_BUTTON_SUBMIT = (
        By.XPATH,
        "//button[text()='Log in']",
        "Login button to submit credentials")

    LOGIN_ERROR = (
        By.XPATH,
        "//div[text()='Your email and/or password are incorrect. Please try again (make sure your caps lock is off).']",
        "Error message when logging in with incorrect data")

    NAVIGATION_USERNAME_BUTTON = (
        By.XPATH,
        "//a[@data-testid='navigation-username-button']",
        "navigation username button")


    PASSWORD_INPUT = (
        By.XPATH,
        "//input[@name='password']",
        "password input")


    # Actions

    def login(self, username, password):
        self.click_on_element(self.LOGIN_BUTTON_FOR_DIALOGUE)
        self.fill_input_field(self.EMAIL_INPUT, username)
        self.click_on_element(self.CONTINUE_WITH_EMAIL_BUTTON)
        self.fill_input_field(self.PASSWORD_INPUT, password)
        self.click_on_element(self.LOGIN_BUTTON_SUBMIT)

    def default_login(self):
        self.login(get_property('FBKR_USER'),get_property('FBKR_USER_PASSWORD'))
        self.element_visible_on_page(self.NAVIGATION_USERNAME_BUTTON)

