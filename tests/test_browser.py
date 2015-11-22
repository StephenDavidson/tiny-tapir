import time, unittest
import tiny_tapir
from selenium.webdriver.remote.webelement import WebElement
from tests.angular_page import AngularPage


class BrowserTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = tiny_tapir.Browser()
        cls.browser.get('https://www.angularjs.org/')

    def test_clear(self):
        self.browser.click(AngularPage.SEARCH_FIELD)
        self.browser.fill(AngularPage.SEARCH_FIELD, 'null')
        self.browser.clear(AngularPage.SEARCH_FIELD)
        assert self.browser.find(AngularPage.SEARCH_FIELD).get_attribute('value') == ''

    def test_clear_and_fill(self):
        self.browser.click(AngularPage.SEARCH_FIELD)
        self.browser.fill(AngularPage.SEARCH_FIELD, 'null')
        self.browser.clear_and_fill(AngularPage.SEARCH_FIELD, 'this is a test')
        assert self.browser.find(AngularPage.SEARCH_FIELD).get_attribute('value') == 'this is a test'

    def test_fill(self):
        self.browser.click(AngularPage.SEARCH_FIELD)
        self.browser.fill(AngularPage.SEARCH_FIELD, 'this is a test')
        assert self.browser.find(AngularPage.SEARCH_FIELD).get_attribute('value') == 'this is a test'

    def test_find(self):
        assert type(self.browser.find(AngularPage.SEARCH_FIELD)) is WebElement

    def test_finds(self):
        els = self.browser.finds(AngularPage.LINKS)
        assert len(els) > 1
        for el in els:
            assert type(el) is WebElement

    def test_get_text(self):
        assert self.browser.get_text(AngularPage.BASICS_HEADER) == 'The Basics'

    def test_is_disabled(self):
        assert self.browser.is_disabled(AngularPage.SEARCH_FIELD) is False

    def test_is_enabled(self):
        assert self.browser.is_enabled(AngularPage.SEARCH_FIELD) is True

    def test_is_not_present(self):
        assert self.browser.is_not_present(AngularPage.FAKE_ELEMENT) is True

    def test_is_clickable(self):
        assert self.browser.is_clickable(AngularPage.SEARCH_FIELD) is True

    def test_is_invisible(self):
        assert self.browser.is_invisible(AngularPage.HIDDEN_SEARCH_FIELD) is False

    def test_is_visible(self):
        assert self.browser.is_visible(AngularPage.SEARCH_FIELD) is True

    def test_switch_to_new_window(self):
        self.browser.click(AngularPage.MIT_LICENSE)
        self.browser.switch_to_new_window()
        text = self.browser.get_text(AngularPage.Github.LICENSE_TEXT)
        if 'github' in self.browser.current_url:
            self.browser.close()
        assert text == 'LICENSE'

    def test_switch_to_main_window(self):
        self.browser.click(AngularPage.MIT_LICENSE)
        self.browser.switch_to_new_window()
        if 'github' in self.browser.current_url:
            self.browser.close()
        self.browser.switch_to_main_window()
        assert type(self.browser.find(AngularPage.SEARCH_FIELD)) is WebElement

    def test_switch_to_window(self):
        self.browser.click(AngularPage.MIT_LICENSE)
        time.sleep(1)  # Wait for new window to open... normally would use switch to new window
        self.browser.switch_to_window(value=1)
        text = self.browser.get_text(AngularPage.Github.LICENSE_TEXT)
        if 'github' in self.browser.current_url:
            self.browser.close()
        assert text == 'LICENSE'

    def test_js_scroll_click(self):
        self.browser._js_scroll_click(element=self.browser.find(AngularPage.BASICS_HEADER))

    def tearDown(self):
        self.browser.switch_to_main_window()
        self.browser.clear(AngularPage.SEARCH_FIELD)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()