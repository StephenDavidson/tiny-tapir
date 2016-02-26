# pylint: disable=E1002
"""
 Action class, that wraps selenium functionality and extends it
 to include asynchronous use cases.
"""
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from waits import Waits
import time


class Actions(object):
    """
    :param driver: Selenium webdriver
    """
    def __init__(self, driver):
        self._driver = driver
        self._waits = Waits(self._driver)

    def clear(self, locator, timeout=60):
        """
        Clear element given a locator pattern
        :param locator: Locator pattern to find element.
                        Format is (selenium.webdriver.common.by.By, Locator)
        :param timeout: Seconds until TimeoutException is thrown
        """
        self._waits.wait_for_element_to_be_clickable(locator, timeout)
        element = self.find(locator)
        element.clear()
        if element.text is not '':
            element.send_keys('')

    def clear_and_fill(self, locator, value, timeout=60):
        """
        Clear element then enter text into an element found using the given locator
        :param value: String to enter into element
        :param locator: Locator pattern to find element.
                        Format is (selenium.webdriver.common.by.By, Locator)
        :param timeout: Seconds until TimeoutException is thrown
        """
        self._waits.wait_for_element_to_be_present(locator, timeout)
        element = self.find(locator)
        element.clear()
        count = 0
        while (element.get_attribute('value') != '') and (count < timeout):
            time.sleep(1)
            element.clear()
            count += 1
        element.send_keys(value)

    def click(self, locator, timeout=60):
        """
        Click element using given locator pattern
        :param locator: Locator pattern to find element.
                        Format is (selenium.webdriver.common.by.By, Locator)
        :param timeout: Seconds until TimeoutException is thrown
        """
        self._waits.wait_for_element_to_be_clickable(locator, timeout)
        element = self.find(locator)
        try:
            element.click()
        except WebDriverException:
            self._js_scroll_click(element)

    def fill(self, locator, value, timeout=60):
        """
        Enter text into an element found using the given locator
        :param value: String to enter into element
        :param locator: Locator pattern to find element.
                        Format is (selenium.webdriver.common.by.By, Locator)
        :param timeout: Seconds until TimeoutException is thrown
        """
        self._waits.wait_for_element_to_be_present(locator, timeout)
        self.find(locator).send_keys(value)

    def find(self, locator, timeout=60):
        """
        Find element given locator pattern
        :param locator: Locator pattern to find element.
                        Format is (selenium.webdriver.common.by.By, Locator)
        :param timeout: Seconds until TimeoutException is thrown
        :return: Webriver element
        """
        self._waits.wait_for_element_to_be_present(locator, timeout)
        return self._driver.find_element(*locator)

    def finds(self, locator, timeout=60):
        """
        Find list of elements given an element locator pattern
        :param locator: Locator pattern to find element.
                        Format is (selenium.webdriver.common.by.By, Locator)
        :param timeout: Seconds until TimeoutException is thrown
        :returns: list of Webdriver elements
        """
        self._waits.wait_for_element_to_be_present(locator, timeout)
        return self._driver.find_elements(*locator)

    def get_text(self, locator, timeout=60):
        """
        Get text from given element locator pattern
        :param locator: Locator pattern to find element.
                        Format is (selenium.webdriver.common.by.By, Locator)
        :param timeout: Seconds until TimeoutException is thrown
        :return: element text
        """
        self._waits.wait_for_element_to_be_present(locator, timeout)
        return self.find(locator).text

    def is_clickable(self, locator, timeout=60):
        """
        Returns true if element is clickable
        :param locator: Locator pattern to find element.
                        Format is (selenium.webdriver.common.by.By, Locator)
        :param timeout: Seconds until TimeoutException is thrown
        :return: Boolean: True if element is clickable, else False
        """
        try:
            self._waits.wait_for_element_to_be_clickable(locator, timeout)
            return True
        except TimeoutException:
            return False

    def is_disabled(self, locator, timeout=60):
        """
        Returns true if element is disabled
        :param locator: Locator pattern to find element.
                        Format is (selenium.webdriver.common.by.By, Locator)
        :param timeout: Seconds until TimeoutException is thrown
        :return: Boolean: True if element is disabled, else False
        """
        self._waits.wait_for_element_to_be_present(locator, timeout)
        return not self.find(locator).is_enabled()

    def is_enabled(self, locator, timeout=60):
        """
        Returns true if element is enabled
        :param locator: Locator pattern to find element.
                        Format is (selenium.webdriver.common.by.By, Locator)
        :param timeout: Seconds until TimeoutException is thrown
        :return: Boolean: True if element is enabled, else False
        """
        self._waits.wait_for_element_to_be_present(locator, timeout)
        return self.find(locator).is_enabled()

    def is_invisible(self, locator, timeout=60):
        """
        Returns true if element is not visible
        :param locator: Locator pattern to find element.
                        Format is (selenium.webdriver.common.by.By, Locator)
        :param timeout: Seconds until TimeoutException is thrown
        :return: Boolean: True if element is not displayed, else False
        """
        self._waits.wait_for_element_to_not_be_visible(locator, timeout)
        try:
            return self._driver.find_element(*locator).is_displayed()
        except NoSuchElementException:
            return True

    def is_not_present(self, locator, timeout=60):
        """
        Returns true if element is not present
        :param locator: Locator pattern to find element.
                        Format is (selenium.webdriver.common.by.By, Locator)
        :param timeout: Seconds until TimeoutException is thrown
        """
        self._waits.wait_for_element_to_not_be_present(locator, timeout)
        try:
            self._driver.find_element(*locator)
            return False
        except NoSuchElementException:
            return True

    def is_selected(self, locator, timeout=60):
        """
        Returns true if element is selected
        :param locator: Locator pattern to find element.
                        Format is (selenium.webdriver.common.by.By, Locator)
        :param timeout: Seconds until TimeoutException is thrown
        :return: Boolean: True if element is selected, else False
        """
        self._waits.wait_for_element_to_be_present(locator, timeout)
        return self.find(locator).is_selected()

    def is_visible(self, locator, timeout=60):
        """
        Returns true if element is visible
        :param locator: Locator pattern to find element.
                        Format is (selenium.webdriver.common.by.By, Locator)
        :param timeout: Seconds until TimeoutException is thrown
        :return: Boolean: True if element is displayed, else False
        """
        self._waits.wait_for_element_to_be_visible(locator, timeout)
        return self.find(locator).is_displayed()

    def switch_to_new_window(self, value=1, timeout=60):
        """
        :param value: Integer window handle value to switch to, defaults to 1
        :param timeout: Seconds until TimeoutException is thrown
        """
        self._waits.wait_for_new_window(timeout)
        self.switch_to_window(value)

    def switch_to_main_window(self, value=0):
        """
        Switch to default window
        :param value:  Integer window handle value to switch to, defaults to 0
        """
        self.switch_to_window(value)

    def switch_to_window(self, value):
        """
        Switches to given window value
        :param value: Integer window handle value to switch to
        """
        window = self._driver.window_handles[value]
        self._driver.switch_to.window(window)

    def _js_scroll_click(self, element):
        """
        Scroll element into view with javascript. Helps with Internet Explorer compatibility
        :return:
        """
        self._driver.execute_script(
            "return arguments[0].scrollIntoView();", element
        )
        time.sleep(1)
        element.click()