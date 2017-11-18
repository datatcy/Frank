# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 22:59:31 2017

@author: FPaulraj
"""
val_tuple=()
if not val_tuple:
    print("This is empty tupple")
val_tuple=("sword","armor","shile","thaling potion")

print("val_tuple",val_tuple)
print("\n===========================")
for j in len(val_tuple)-1:
    for i in val_tuple:
        print(i,"    ",val_tuple[j])
input("enter any key to exit")

