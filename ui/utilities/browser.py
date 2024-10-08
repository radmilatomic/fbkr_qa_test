import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

CHROME = 'chrome'
FIREFOX = 'firefox'

INCOGNITO = "--incognito"
HEADLESS_OPT = '--headless'

global WEB_DRIVER


def create_new_driver(driver_name, mode="head"):
    if driver_name == CHROME:
        chrome_options = ChromeOptions()
        chrome_options.add_argument(INCOGNITO)
        chrome_options.add_argument("--start-maximized")
        if mode == "headless":
            chrome_options.add_argument(HEADLESS_OPT)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    elif driver_name == FIREFOX:
        firefox_options = FirefoxOptions()
        if mode == "headless":
            firefox_options.add_argument(HEADLESS_OPT)

        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)
        driver.maximize_window()
    else:
        raise Exception("There is no support for {} browser".format(driver_name))
    global WEB_DRIVER
    WEB_DRIVER = driver


def shut_down():
    WEB_DRIVER.quit()


def open_url(url):
    WEB_DRIVER.get(url)
    wait_for_page_to_load()


def switch_to_latest_window():
    windows = WEB_DRIVER.window_handles
    if len(windows) == 1:
        WEB_DRIVER.switch_to.window(windows[0])
    else:
        WEB_DRIVER.switch_to.window(windows[-1])


def wait_for_page_to_load():
    old_page = WEB_DRIVER.find_element_by_tag_name('html')
    yield
    WebDriverWait(WEB_DRIVER, 10).until(staleness_of(old_page))


def sleep_for_n_seconds(seconds):
    time.sleep(seconds)
