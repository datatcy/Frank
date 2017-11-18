# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 20:55:14 2017

@author: FPaulraj
"""

geek={"404":"clueless. From the web error message 404, meaning page not found.",
      "gogling":"searching the internet for background information on a person.",
      "keyboard plaque":"the collection ofdebris found in computer keyboards.",
      "Link Rot":"the process by which web page linkbecome obsolete.",
      "Percussive Maintenance":"the act of striking an electronic device to make it work",
      "Uninstalled":"being fired.  Especially popular during the bot-bomb era"}
choice=None
while choice !="0":
    print(""" 
          0 - Exit
          1 - Lookup up a Geek Term
          2 - Add a Geek Term
          3 - Redefine a Geek Term
          4 - Delete a Geek Term
          """
          )
    choice=input("Enter your choice:  ")
    print()
    if choice =="0":
        print("Exit the programe,'GOOD BYE'")
    elif choice == "1":
        key=input("Enter the KEY to get the value: ")
        if key in geek:
            print(geek[key])
        else:
            print("Not valid KEY")
    elif choice =="2":
        key=input("Enter KEY to add definition: ")
        if key not in geek:
            definition=input("Enter definition for the KEY ")
            geek[key]=definition
            print(key,"   ", definition, "added to geek\n")
        else:
            print("KEY is already exist")
    elif choice =="3":
        key=input("Enter the KEY to be redifined: ")
        if key in geek:
            definition=input("Enter the definition for the KEY: ")
            print(key)
            geek[key]=definition
            print(key, "has been redifined")
        else:
            print("The KEY dosent exist")
    elif choice =="4":
        key=input("Enter KEY to be deleted: ")
        if key in geek:
            del geek[key]
            print(key,"has been deleted from dictinory")
        else:
            print("entery correct key")
    elif choice =="5":
        #print(geek) 
        #print("Keys are\n")
      #  print(geek.keys(),"\n")
       # print("values are \n")
       # print(geek.values(),"\n")
        lenkey=len(geek)
        keys=geek.keys()
        vals=geek.values()
        for keys in geek:
            print(keys,"\t",geek.get(keys))
    else:
        print("not correct choice")
input("Eter any key to exist")
        
    
        
    
            
    
    
