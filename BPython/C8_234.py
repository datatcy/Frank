# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 22:21:23 2017

@author: FPaulraj
"""

# CREATING PRIVATE AND PUBLIC ATTRIBUTE AND METHODS

class Critter(object):
    def __init__(self,name,mood):
        print("Public and Private attributes \n")
        self.name=name
        self.__mood=mood
    
    def talk(self):
        print("Public Attribute ",self.name,"\n")
        print("Private Attribute ",self.__mood,"\n")
        
    def __pvtmethod(self):
        print("This is Private Method",self.__mood)
    def pubmethod(self):
        print("This is Public Method",self.name,"private atribute",self.__mood)
        self.__pvtmethod()
# Main
crit=Critter(name="pub",mood="pvt")
print("Public object constructor attribute is ",crit.name)
#print("Private object constructor attribute is ",crit.mood,"\n") --> will give error
print("Accessing private attribute through publec method ")
crit.talk()
print("accessing private method thorugh public nethod \n")
crit.pubmethod()
print("accessing private method through object\n")
##crit.__pvtmethod()  ---> this will throw error
print("Accessing Private attribute outside of class ",crit._Critter__mood,"\n")
print("Accessing Private Method outside of class ")
crit._Critter__pvtmethod()




input("Enter any key to exit")
        