# -*- coding: utf-8 -*-

import unittest
import os
from mess import *

class Test(unittest.TestCase):  


    def testParse(self):
        thisFileDir = os.path.dirname(__file__)
        
        wordInValue = u'[сС][дД][еЕ][лЛ]'
        wordForReplace = u'УРА'
        encoding = 'cp1251'

        messList = parse(thisFileDir, wordInValue, wordForReplace, encoding)
        toFile(os.path.join(thisFileDir, 'messOut.html'), buildHtml(messList, u'Найденный список'), 'UTF-8')