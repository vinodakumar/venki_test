# -*- coding: utf-8 -*-
"""
Created on Mon May 29 23:06:32 2017

@author: vinodakumar
"""

import unittest 
class basetest(unittest.TestCase):
    var=10
    def setUp(self):
        self.a=10
        self.b=20
        
    def teardown(self):
        print("we are in teardown")
        
    def test_addition(self):
        print('addition: ', self.a+self.b)
        assert self.a==self.a+self.b

    def test_multiplication(self):
        print('multiplication: ', self.a*self.b)
        assert self.a==self.a+self.b
    
    def test_substraction(self):
        print('substraction: ', self.a-self.b)
        assert self.a==self.a+self.b
    
    def test_division(self):
        print('division: ', self.a/self.b)
        assert self.a==self.a+self.b
    
    
