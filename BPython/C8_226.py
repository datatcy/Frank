# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 20:57:09 2017

@author: FPaulraj
"""

# CONSTRUCTOR METHOD

class Critter(object):
    def __init__(self, name):
        print("New object has been born: \n")
        self.name=name
    def __str__(self):
        #print("object in constructor method :\n")
        #print("object argument is ",self.name,"\n")
        ref ="Object in constructor method "
        ref +="name:"+ self.name
        return ref
    def talk(self):
        print("Hi, I am",self.name,"\n")
#main
cls=Critter("Francis")
cls.talk()
print("Directly accessing Object attribute ", cls.name,"\n")
print("Diretly printing ",cls,"\n")

input("enter any key to exit")