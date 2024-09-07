import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, test_name):
        """
        Base class is serving basic attributes for every single page inherited from Page class
        :param driver: driver used for manipulation with web browser
        """
        self.driver = driver
        self.test_name = test_name
        self.timeout = 30
        self.default_wait_in_seconds = 10

    # Actions

    def assert_msg(self, message):
        self.driver.get_screenshot_as_file(f"../../test_reports/{self.test_name}.png")
        return message

    def click_on_element(self, locator):
        """
        Wait until element is clickable and click on it
        :param locator: Web element locator.
        :return:
        """
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((locator[0], locator[1])),
                                             message="ELEMENT NOT FOUND OR NOT CLICKABLE: {0}".format(
                                                 locator[2])).click()

    def default_wait(self, default_wait_time=1):
        time.sleep(default_wait_time)

    def element_not_visible_on_page(self, locator):
        """
        Confirm that element is not visible on page
        :param locator: Web element locator.
        :return: Boolean
        """
        return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((locator[0], locator[1])),
                                                    message="ELEMENT SHOULD NOT BE VISIBLE: {0}".format(locator[2]))

    def element_visible_condition(self, locator):
        """
        Used when test continues after element visible check.
        :param locator: Web element locator.
        :return: Boolean
        """
        try:
            return WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located((locator[0], locator[1]))).is_displayed()
        except TimeoutException:
            return False

    def element_visible_on_page(self, locator):
        """
        Confirm that element is visible on page
        :param locator: Web element locator.
        :return: Boolean
        """
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((locator[0], locator[1])),
                                                    message="ELEMENT NOT VISIBLE: {0}".format(
                                                        locator[2])).is_displayed()

    def fill_input_field(self, locator, text):
        self.click_on_element(locator)
        input_element = self.find_element(locator)
        input_element.send_keys(Keys.LEFT_CONTROL, "a")
        input_element.send_keys(Keys.DELETE)
        self.default_wait(1)
        input_element.send_keys(text)

    def find_element(self, locator):
        """
        Find an element on a web page using provided locator.
        :param locator: Web element locator.
        :return: WebElement
        """
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((locator[0], locator[1])),
                                                    message="ELEMENT NOT FOUND: {0}".format(locator[2]))

    def find_elements(self, locator):
        """
        Find an element on a web page using provided locator.
        :param locator: Web element locator.
        :return: list of WebElements
        """
        try:
            return WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((locator[0], locator[1])),
                                                        message="ELEMENT NOT FOUND: {0}".format(locator[2]))
        except TimeoutException:
            return []

    def loading_done(self, locator):
        """
        Wait until loading element disappears from screen
        :param locator: Web element locator.
        :return: Boolean
        """
        self.default_wait(2)  # added for firefox slow response
        return WebDriverWait(self.driver, 60).until(EC.invisibility_of_element_located((locator[0], locator[1])),
                                                    message="ELEMENT STILL VISIBLE: {0}".format(locator[2]))
