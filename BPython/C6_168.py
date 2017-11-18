# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 14:22:58 2017

@author: FPaulraj
"""
#   EXAMPLE FOR ENCAPSULATION AND SCOPE
def hb1(name,age):
    print("Happy Birthday to ",name,"Today you are turned to",age)
def hb2(name="francis", age=16):
    print("Happy Birthday to ",name,"Today you are turned to ",age)
def call_global():
    print("Value of global variable call inside call_global()",value,"\n")
def call_global_shadow():
    value=-10
    print("Call local variable in call_global_shadow() with same name in global",value,"\n")
def call_global_chage():
    global value
    value=124
    print("Chage the global variable Value in side call_global_chage() and modifiy",value,"\n")
 
# Main
value =20

hb1("francis","1")
hb1("1","francis")
hb1(name="xxxx",age="23")
hb1(age="xxyy",name="100")
print("\n")
hb2()
hb2("francis","1")
hb2(name="SS")
hb2(age=23)
print("\n")
call_global()
print("No change in global variale",value,"\n")
call_global_shadow()
print("No change in global variabvle", value,"\n")
call_global_chage()
print("Global variable value changeed",value)

