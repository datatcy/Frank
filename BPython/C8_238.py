# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 20:56:24 2017

@author: FPaulraj
"""

# TO ACCESS PRIVATE ATTRIBUTE AND METHOD INDIRECTILY THROUGHH PROPERTY
class Critter(object):
    def __init__(self,name):
        print("New critter has been boarn\n")
        self.__name=name
        #call this pvt attributre through method property with the same name like attribute 'name'
    @property    
    def name(self):
        return self.__name
    @name.setter #to change the private attribute throiugh propertity method
    def name(self,new_name):
        if new_name =="":
            print("Name can not be null \n")
        else:
            self.__name=new_name
            print("New name has been change    ",self.__name)
    def talk(self):
        print("Hi i am ", self.name)
# Main
crit=Critter("francis")
crit.talk() # calls the private attribute indirtely calling its property method through method
print("Accessing pvt attribute through its property: ",crit.name)
print("Attempting to change the private attribute\n")
crit.name="Francis Paulraj"
print(crit.name)
crit.talk()
crit.name=""


