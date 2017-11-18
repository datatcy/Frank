# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 21:34:35 2017

@author: FPaulraj
"""
import random
#Ramdon access
word="index"
print("the word is",word)
high=len(word)
low= -len(word)
print(high,"   ",low)

for i in range(10):
    position=random.randrange(low,high)
    print("word[",position,"]\t",word[position])


input("enter any key to exit")