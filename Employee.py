# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 11:58:37 2020

@author: abhishekar
"""

class Employee:
    def __init__(self, empId, name):
       self.__empId = empId
       self.__name = name
        
    def __repr__(self):
        return "{}".format(self.__name)
    
    def get_id(self):
        return self.__empId
        
    def __str__(self):
        return self.__empId + ", " + self.__name
    
    @property
    def empId(self):
        return self.__empId
    
    @empId.setter
    def empId(self, value):
        self.__empId = value
        
    @empId.deleter
    def empId(self):
        del self.__empId
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def empId(self, value):
        self.__name = value
        
    @name.deleter
    def empId(self):
        del self.__name