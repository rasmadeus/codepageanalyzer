# -*- coding: utf-8 -*-

import unittest
import os
from checker.check import *

class Test(unittest.TestCase):  


    def testParse(self):
        thisFileDir = os.path.dirname(__file__)