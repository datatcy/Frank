# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 21:52:44 2017

@author: FPaulraj
"""

print("Exclusive Computer Network")

security=0
username=""

while not username:
    username=input("username:  ")
password=""
while not password:
    password=input("password: ")
if username=="M.Dawson" and password=="secret":
    print("Hi, Mike")
    security=2
elif username=="S.Miyamot" and password=="mariobros":
    print("What's up, Shigeru?")
else:
    print("login failed") 
input("Enter any key to exist")