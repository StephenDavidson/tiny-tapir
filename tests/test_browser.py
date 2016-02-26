import unittest
from tiny_tapir import Browser
from tests.angular_page import AngularPage


class BrowserTest(unittest.TestCase):
    # Disabled for CI
    def _chrome(self):
        b = Browser(name='chrome')
        b.driver.get('https://www.angularjs.org/')
        b.click(AngularPage.SEARCH_FIELD)
        b.driver.quit()

    def test_firefox(self):
        b = Browser()
        b.driver.get('https://www.angularjs.org/')
        b.click(AngularPage.SEARCH_FIELD)
        b.driver.quit()