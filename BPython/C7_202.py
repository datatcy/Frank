# -*- coding: utf-8 -*
"""
Created on Sat Aug 12 21:43:20 2017

@author: FPaulraj
"""

# PICKLE PROGRAM
import pickle,shelve
bd=open("pickle.dat","wb")
varity=["sweet","hot","dill"]
shape=["whole","spear","chip"]
brand=["Claussen","Heinz","classic"]
pickle.dump(varity,bd)
pickle.dump(shape,bd)
pickle.dump(brand,bd)
bd.close()
print("UNPACKING PICKLE")
bd=open("pickle.dat","rb")
varity=pickle.load(bd)
print(varity)
bd.close()

print("SHELVING")
s=open("pickle.dat")
s["varity"]=["sweet","hot","dill"]
s["shape"]=["whole","spear","chip"]
s["brand"]=["Claussen","Heinz","classic"]
s.sync()

