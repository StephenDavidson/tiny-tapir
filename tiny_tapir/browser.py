# pylint: disable=E1002
"""
 Browser class, that wraps selenium functionality and extends it
 to include asynchronous use cases.
"""
from selenium import webdriver
from tiny_tapir.actions import Actions


BROWSERS = {
    'chrome': webdriver.Chrome,
    'firefox': webdriver.Firefox,
    'ie': webdriver.Ie
}


class Browser(Actions):
    """
    Return browser with given name
    :param name: Browser to return, defaults to firefox
    :param *args: Browser arguments
    :param **kwargs: Browser kwarguments
    """
    def __init__(self, name='firefox', *args, **kwargs):
        self.driver = BROWSERS[name.lower()](*args, **kwargs)
        super(Browser, self).__init__(self.driver)
