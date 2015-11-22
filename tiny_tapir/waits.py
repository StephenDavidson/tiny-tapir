"""
    Waits class that wraps selenium webdriver waits into a readable format.
"""
import logging, time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOG = logging.getLogger(__name__)


class Waits(object):
    """
        Wrapper for readable selenium waits
        Argument:
        Selenium Wedriver
    """
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_to_be_present(self, locator, timeout=60):
        """
        :param timeout: Seconds before timeout exception is thrown
        """
        LOG.debug('Waiting for element to be present by locator strategy ' + str(locator))
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_element_to_not_be_present(self, locator, timeout=60):
        """
        :param timeout: Seconds before timeout exception is thrown
        """
        LOG.debug('Waiting for element to not be present by locator strategy ' + str(locator))
        WebDriverWait(self.driver, timeout).until_not(
            EC.presence_of_element_located(locator)
        )

    def wait_for_element_to_be_visible(self, locator, timeout=60):
        """
        :param timeout: Seconds before timeout exception is thrown
        """
        LOG.debug('Waiting for element to NOT be visible by locator strategy ' + str(locator))
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_element_to_not_be_visible(self, locator, timeout=60):
        """
        :param timeout: Seconds before timeout exception is thrown
        """
        LOG.debug('Waiting for element to be visible by locator strategy ' + str(locator))
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def wait_for_element_to_be_clickable(self, locator, timeout=60):
        """
        :param timeout: Seconds before timeout exception is thrown
        """
        LOG.debug('Waiting for element to be clickable by locator strategy ' + str(locator))
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_element_to_not_be_clickable(self, locator, timeout=60):
        """
        :param timeout: Seconds before timeout exception is thrown
        """
        LOG.debug('Waiting for element to NOT be clickable by locator strategy ' + str(locator))
        WebDriverWait(self.driver, timeout).until_not(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_alert_present(self, timeout=60):
        """
        :param timeout: Seconds before timeout exception is thrown
        """
        LOG.debug('Waiting for alert to be present')
        WebDriverWait(self.driver, timeout).until(
            EC.alert_is_present()
        )

    def wait_for_alert_not_present(self, timeout=60):
        """
        :param timeout: Seconds before timeout exception is thrown
        """
        LOG.debug('Waiting for alert to NOT be present')
        WebDriverWait(self.driver, timeout).until_not(
            EC.alert_is_present()
        )

    def wait_for_new_window(self, timeout=60):
        """
        :param timeout: Seconds before timeout exception is thrown
        :return True if new window or tab opens
        """
        LOG.debug('Waiting new window/tab to open')
        while timeout:
            if len(self.driver.window_handles) > 1:
                break
            time.sleep(1)
            timeout -= 1
        if len(self.driver.window_handles) == 1:
            Exception('New window never appeared after waiting ' + str(timeout) + ' seconds')
