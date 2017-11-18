# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 22:14:28 2017

@author: FPaulraj
"""

msg=input("enter any string")
VOWELS="aeiou"
new_msg=" "
print()
for letter in msg:
    if letter.lower() not in VOWELS:
        new_msg +=letter
        print("msg with no vowels",new_msg, "letter first",letter)
    print("msg with",new_msg)
print("msg",new_msg)

input("enter any key to exist")