from selenium.webdriver.common.by import By


class AngularPage(object):
    PATH = ''

    BASICS_HEADER = (By.ID, 'the-basics')
    FAKE_ELEMENT = (By.ID, 'this_does_not_exist')
    HIDDEN_SEARCH_FIELD = (By.NAME, 'as_sitesearch')
    LINKS = (By.TAG_NAME, 'a')
    MIT_LICENSE = (By.PARTIAL_LINK_TEXT, 'MIT')
    SEARCH_FIELD = (By.NAME, 'as_q')

    class Github:
        LICENSE_TEXT = (By.CLASS_NAME, 'final-path')