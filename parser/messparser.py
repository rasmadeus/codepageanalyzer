#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Aug 6, 2015
'''

from pyparsing import Word, alphas, ZeroOrMore, printables, OneOrMore, alphanums, Regex

class MessParser: 
    
    def init(self, out_file):
        self._out_file = out_file
        self._res = {}
    
    def parse(self, in_file):
        pass
    
    def _parse(self, in_data):
        rus_alphas = "йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"
        symbols = ".,!~@#$%^&*()_-+=?/\\ "
        any = alphanums + rus_alphas + symbols
        
        word = Word("$MESS[\"") + Word(any) + Word("\"]") + ZeroOrMore(" ") + Word("=") + ZeroOrMore(" ") + Word("\"") + Word(any) + Word("\"")
        return word.parseString(in_data).asList()
