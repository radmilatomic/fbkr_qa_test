import pytest

from libraries.logger import Logger
from ui.utilities import browser

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome')
    parser.addoption('--mode', action='store', default='head')


@pytest.fixture(scope="function")
def setup(request):
    logger = Logger()
    Logger.log_set_up(logger, request.node.name)
    request.cls.logger = logger

    browser_name = request.config.getoption('browser')
    mode = request.config.getoption('mode')

    browser.create_new_driver(browser_name, mode)

    Logger.log_method_name(logger, request.node.name)

    browser.open_url("https://fishingbooker:QAFBTest@qahiringtask.dev.fishingbooker.com")
    browser.sleep_for_n_seconds(2)
    browser.open_url("https://qahiringtask.dev.fishingbooker.com")

    yield
    Logger.log_tear_down(logger, request.node.name)
    browser.shut_down()
    logger.remove_handlers()



