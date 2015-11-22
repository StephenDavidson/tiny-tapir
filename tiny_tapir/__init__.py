"""
    Asynchronous selenium wrapper
"""
__author__ = 'Stephen'

from .browser import Browser

# Logger
import logging

try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        """ Return null handler"""
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
