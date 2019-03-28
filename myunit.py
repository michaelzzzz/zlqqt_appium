import unittest
from time import sleep

from zlqqt_desired_caps import logging, zlqqt_desired


class StartEnd(unittest.TestCase):

    def setUp(self):
        logging.info('==================setUp=====================')
        self.driver = zlqqt_desired()

    def tearDown(self):
        logging.info('==================tearDown==================')
        sleep(5)
        self.driver.close_app()