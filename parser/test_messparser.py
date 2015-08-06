#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Aug 6, 2015

'''
import unittest

from messparser import MessParser

class  TestParser(unittest.TestCase):

    def test_find_all_common_parts(self):
        messparser = MessParser()   
           
        data = (     
            "$MESS[\"USER_TYPE_CRM_DESCRIPTION\"] = \"Прив СделКаэлементам CRM\"",
            "$MESS[\"USER_TYPE_CRM_DESCRIPTION\"] = \"фффПрив\"",
            "$MESSUSER_TYPE_CRM_DESCRIPTION\"] = \"Приfffв\"",
            "$MESS[\"USER_TYPE_CRM_DESCRIPTION\"] = \"Прив SделКаэлементам CRM\"",
            "$MESS[\"USER_TYPE_CRM_DESCRIPTION\"] = \"ПфываСделКафываM\"",
            "$MESS[\"USER_TYPE_CRM_DESCRIPTION\"] = \"сделКа\"",
        )

        expected_res = [[data[0],], [], [], [], [data[4],], [data[5],]]
        real_res = [messparser._find_all_common_parts(in_data) for in_data in data]

        self.assertEquals(real_res, expected_res)
        
        
    def test_file_reading(self):
        import os
        relative_path_to_test_file = 'test{separator}data{separator}test_file.txt'.format(separator=os.sep)
        path_to_test_file = os.path.join(os.path.dirname(__file__), relative_path_to_test_file)

        messparser = MessParser()
        file_data = messparser._get_in_data(path_to_test_file)
        common_parts = messparser._find_all_common_parts(file_data)
        print(file_data)
        print(common_parts)
