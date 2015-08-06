#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Aug 6, 2015
'''

import re

class MessParser: 
    
    def init(self, out_file):
        self._out_file = out_file
        self._res = {}
    
    def parse(self, in_file):     
        common_parts = self._find_all_common_parts(self._get_in_data(in_file))
            

    def _get_in_data(self, in_file):
        try:
            res = ''
            for line in open(in_file).read().splitlines():
                res += line
            return res
        except IOError as ex:
            print('Cannot read data from {file}'.format(file=in_file))
            return ''
    
    def _find_all_common_parts(self, in_data):
        wordInResult = '[сС][дД][еЕ][лЛ]'
        pattern = '\\$MESS\S+ += +".*{word}.*"'.format(word=wordInResult)
        return re.compile(pattern).findall(in_data)
        
