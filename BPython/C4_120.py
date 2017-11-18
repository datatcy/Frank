# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 19:37:21 2017

@author: FPaulraj
"""

# Print the user entered message in reverse

msg=input("Enter any message  ")
LnMsg=len(msg)-1
print(LnMsg)
#print(msg[7])

for i in range(LnMsg,-1,-1):
    print(i, end="|")
    print(msg[i], end=" ")

print("\n",msg, end=" ")

input("\nEnter any key to exit")