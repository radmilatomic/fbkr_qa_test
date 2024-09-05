from selenium.webdriver.common.by import By

from ui.pages.base_page import BasePage


class LoginPage(BasePage):
    # Locators
    LOGIN_BUTTON_FOR_DIALOGUE = (
        By.XPATH,
        "//p[contains(text(),'Log in')]",
        "Login button to open login dialogue")

    EMAIL_INPUT = (
        By.XPATH,
        "//input[@name='email']",
        "email input")

    PASSWORD_INPUT = (
        By.XPATH,
        "//input[@name='password']",
        "password input")

    CONTINUE_WITH_EMAIL_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Continue with email')]",
        "Continue with email button")

    LOGIN_BUTTON_SUBMIT = (
        By.XPATH,
        "//button[text()='Log in']",
        "Login button to submit credentials")

    NAVIGATION_USERNAME_BUTTON = (
        By.XPATH,
        "//a[@data-testid='navigation-username-button']",
        "navigation username button")

    # Actions
    def login(self):
        self.click_on_element(self.LOGIN_BUTTON_FOR_DIALOGUE)
        self.fill_input_field(self.EMAIL_INPUT, 'rada1007+2@gmail.com')
        self.click_on_element(self.CONTINUE_WITH_EMAIL_BUTTON)
        self.fill_input_field(self.PASSWORD_INPUT, 'fbkrqatestpass')
        self.click_on_element(self.LOGIN_BUTTON_SUBMIT)
        self.element_visible_on_page(self.NAVIGATION_USERNAME_BUTTON)
        # browser.open_url('https://qahiringtask.dev.fishingbooker.com')
