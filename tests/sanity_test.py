"""
Ensure the environment is sane
"""

import unittest
import webtest
import jinja2

from google.appengine.api import memcache
from google.appengine.ext import db
from google.appengine.ext import testbed

from src import main


class SanityTest(unittest.TestCase):

    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()

    def tearDown(self):
        self.testbed.deactivate()

    def test_sanity(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
