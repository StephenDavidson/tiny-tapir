import time, unittest
from tiny_tapir import actions
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from tests.angular_page import AngularPage


class BrowserTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Firefox()
        cls.actions = actions.Actions(cls.browser)
        cls.browser.get('https://www.angularjs.org/')

    def test_clear(self):
        self.actions.click(AngularPage.SEARCH_FIELD)
        self.actions.fill(AngularPage.SEARCH_FIELD, 'null')
        self.actions.clear(AngularPage.SEARCH_FIELD)
        assert self.actions.find(AngularPage.SEARCH_FIELD).get_attribute('value') == ''

    def test_clear_and_fill(self):
        self.actions.click(AngularPage.SEARCH_FIELD)
        self.actions.fill(AngularPage.SEARCH_FIELD, 'null')
        self.actions.clear_and_fill(AngularPage.SEARCH_FIELD, 'this is a test')
        assert self.actions.find(AngularPage.SEARCH_FIELD).get_attribute('value') == 'this is a test'

    def test_fill(self):
        self.actions.click(AngularPage.SEARCH_FIELD)
        self.actions.fill(AngularPage.SEARCH_FIELD, 'this is a test')
        assert self.actions.find(AngularPage.SEARCH_FIELD).get_attribute('value') == 'this is a test'

    def test_find(self):
        assert type(self.actions.find(AngularPage.SEARCH_FIELD)) is WebElement

    def test_finds(self):
        els = self.actions.finds(AngularPage.LINKS)
        assert len(els) > 1
        for el in els:
            assert type(el) is WebElement

    def test_get_text(self):
        assert self.actions.get_text(AngularPage.BASICS_HEADER) == 'The Basics'

    def test_is_disabled(self):
        assert self.actions.is_disabled(AngularPage.SEARCH_FIELD) is False

    def test_is_enabled(self):
        assert self.actions.is_enabled(AngularPage.SEARCH_FIELD) is True

    def test_is_not_present(self):
        assert self.actions.is_not_present(AngularPage.FAKE_ELEMENT) is True

    def test_is_clickable(self):
        assert self.actions.is_clickable(AngularPage.SEARCH_FIELD) is True

    def test_is_invisible(self):
        assert self.actions.is_invisible(AngularPage.HIDDEN_SEARCH_FIELD) is False

    def test_is_visible(self):
        assert self.actions.is_visible(AngularPage.SEARCH_FIELD) is True

    def test_switch_to_new_window(self):
        self.actions.click(AngularPage.MIT_LICENSE)
        self.actions.switch_to_new_window()
        text = self.actions.get_text(AngularPage.Github.LICENSE_TEXT)
        if 'github' in self.browser.current_url:
            self.browser.close()
        assert text == 'LICENSE'

    def test_switch_to_main_window(self):
        self.actions.click(AngularPage.MIT_LICENSE)
        self.actions.switch_to_new_window()
        if 'github' in self.browser.current_url:
            self.browser.close()
        self.actions.switch_to_main_window()
        assert type(self.actions.find(AngularPage.SEARCH_FIELD)) is WebElement

    def test_switch_to_window(self):
        self.actions.click(AngularPage.MIT_LICENSE)
        time.sleep(1)  # Wait for new window to open... normally would use switch to new window
        self.actions.switch_to_window(value=1)
        text = self.actions.get_text(AngularPage.Github.LICENSE_TEXT)
        if 'github' in self.browser.current_url:
            self.browser.close()
        assert text == 'LICENSE'

    def test_js_scroll_click(self):
        self.actions._js_scroll_click(element=self.actions.find(AngularPage.BASICS_HEADER))

    def tearDown(self):
        self.actions.switch_to_main_window()
        self.actions.clear(AngularPage.SEARCH_FIELD)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()