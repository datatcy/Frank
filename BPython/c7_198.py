# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 21:13:15 2017

@author: FPaulraj
"""

# TO WRITE CONTENT IN TO TEXT FILE
txtfile=open("writefile.txt","w")
txtfile.write("Line 1\n Line make two 2\n This make line 3\n")
txtfile.close()
txtfile=open("writefile.txt","r")
print(txtfile.read())
txtfile.close()
wrtline=["Test to write line\n","This line written from list\n","check list wrote\n"]
txtfile=open("writefile.txt","a")
txtfile.writelines(wrtline)
txtfile.close()
