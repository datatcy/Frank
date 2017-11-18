# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 21:34:44 2017

@author: FPaulraj
"""

# EXAMPLE FOR CLASS METHOD OR STATIC METHOD STATIC ATTRIBUTE
class Critter(object):
    total=0
    def status():
        print("The value of static class attribute is : ", Critter.total,"\n")
    def __init__(self,name):
        print("A Critter has been born \n")
        self.name=name
        Critter.total +=1
# main
print("Accessing Class attribute with out creating object class",Critter.total)
print("total count before all object initialization ")
Critter.status()

cri1=Critter("object one")
cri2=Critter("object two")
cri3=Critter("object three")

print("Accessing class attribute through class object",cri1.total,"\n")
print("Accessing class method through class object ",cri1.status)
print("total count after all object initialization ")
Critter.status()
print("Directly accessting constructor attribute through object", cri1.name)

input("Enter any key to exit")

        