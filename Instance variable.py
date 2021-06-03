# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 12:12:00 2021

@author: SST-LAB
"""
#instance method
class student:    
    def __init__(self, a,b):
        self.a = a
        self.b = b
    def avg (self):
      return self.a + self.b
student_1 = student(20, 30)
print (student_1.b)
print (student_1.avg() )



#class method
class student:
    name = "student"
    def __init__ (self, a, b):
        self.a = a
        self.b = b
    @classmethod    
    def info(cls):
        return cls.name
    
    