#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Aug 6, 2015

'''
import unittest

from messparser import MessParser

class  TestParser(unittest.TestCase):

    def test_parser_data(self):
        messparser = MessParser()
        
        test_data = (
            "$MESS[\"USER_TYPE_CRM_DESCRIPTION\"] = \"Привязка к элементам CRM\"",
            "$MESS[\"USER_TYPE_CRM_ENTITY_TYPE\"] = \"Доступная сущность\"",
        )
        
        for data in test_data:
            print(messparser._parse(data))
        
        