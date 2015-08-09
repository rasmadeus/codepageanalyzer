# -*- coding: utf-8 -*-

import unittest
import os
from checker.check import findEncodingErrors, toFile, buildHtml

class Test(unittest.TestCase):  


    def testParse(self):
        thisFileDir = os.path.dirname(__file__)
        mustBeInEncoding = 'UTF-8'
        errors = findEncodingErrors(thisFileDir, mustBeInEncoding)
        resInHtml = buildHtml(errors, u'Найдены несоответствия кодировки')
        toFile(os.path.join(thisFileDir, u'encodingErrors.html'), resInHtml, 'UTF-8')