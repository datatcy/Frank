# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 20:38:40 2017

@author: FPaulraj
"""

txtfile=open("sample.txt","r")
print(txtfile.read(5))
txtfile.close()
txtfile=open("sample.txt","r")
print(txtfile.readline(1))
print(txtfile.readline(5))
txtfile.close()
txtfile=open("sample.txt","r")
readln=txtfile.readlines()
for i in readln:
    print(i)
print(readln)
print(len(readln),"\n")
print(readln[1:3])
for i in range(0,len(readln),2):
    print(readln[i],"  ",i ,"\n")
txtfile.close()

input("enter any key to exit")