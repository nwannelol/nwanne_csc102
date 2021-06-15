# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 15:13:49 2021

@author: SST-LAB
"""

class Student:
     studentLevel = 'first year computer science 2020/2021 session'
     studentCounter = 0
     def __init__(self, thename, thematricno, thesex, hostelname, age, csc102examscore):
         self.name = thename
         self.matricno = thematricno
         self.sex = thesex
         self.hostelname = hostelname
         self.age = age
         self.csc102examscore = csc102examscore
         Student.studentCounter = Student.studentCounter + 1

     def getName(self):
         return  self.name

     def setName(self, thenewName):
         self.name = thenewName

     def getage (self):
        if self.age < 16:
            print(f"{self.name} is younger then 16")
        else:
            print(f"{self.name} is older than 16")





        @staticmethod
        def PAUNanthem():
            print('Pau, here we come, Pau, here we come ')
    

    
     def carryover (self):
      
         if self.csc102examscore < 45:
            print(f"You are carrying over this course")
         else:
            print(f"you be sabi boy")
    



student1 = Student('James Kaka', '021074', 'M', "ämethyst", 17, 89 )
print(student1.getName())
student1.setName('James Gaga')
print(student1.getName())
print(student1.getage())
print(student1.carryover())
print(Student.studentCounter)