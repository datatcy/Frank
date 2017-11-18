# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 22:23:50 2017

@author: FPaulraj
"""

scores=[("Moe",1000),("Larry",1500),("Cury",2000)]
lenth=len(scores)
#for i in scores:
   # print(i,end="\n")
    
for j in range(lenth):
    print(scores[j][0], end="\t")
    print(scores[j][1])

print("NAME\t","SCORE")
print("----\t","-----")
for name, score in scores:
    print(name,"\t",score)
input("Enter any key exit")
