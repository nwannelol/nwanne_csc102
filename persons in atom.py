# -*- coding: utf-8 -*-
"""
Created on Thu May 27 15:13:28 2021

@author: SST-LAB
"""

class person:
    personcount = 0
    def __init__(self, name, age, gang):
        self.name = name
        self.age = age
        self.gang = gang
        person.personcount = person.personcount + 1
        print ("there are {person.personcount} (s)amount of people")
person_1 = person("ken", "21", "blood")
print(person_1.age)
print(person_1.gang)


person_2 = person("chuka", "30", "crip")
print(person_2.name)     