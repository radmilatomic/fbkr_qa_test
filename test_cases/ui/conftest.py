import pytest

from libraries.logger import Logger
from ui.utilities import browser
from libraries.properties import get_property

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
    url_with_credentials = get_property('FBKR_QA_INSTANCE_WITH_CREDENTIALS')
    url = get_property('FBKR_QA_INSTANCE')

    browser.open_url(url_with_credentials)
    browser.sleep_for_n_seconds(2)
    browser.open_url(url)

    yield
    Logger.log_tear_down(logger, request.node.name)
    browser.shut_down()
    logger.remove_handlers()



