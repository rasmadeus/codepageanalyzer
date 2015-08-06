#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Aug 6, 2015
'''

import os
from parser.messparser import MessParser

class Collector(object):

    def __init__(self, initial_dir, dest_file):
        self._parser = MessParser(dest_file)
        self._initial_dir = initial_dir
        
    def start(self):
        self._walk(self._initial_dir)                
    
    def _walk(self, initial_dir):
        for dir_path, dirs, files in os.walk(initial_dir):
            for file_path in files:
                self._parser.parse(os.path.join(dir, file_path))
            for subdir in dirs:
                self._walk(os.path.join(dir_path, subdir))
                
        
        