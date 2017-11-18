# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 21:13:31 2017

@author: FPaulraj
"""

#List Programe
sorts=[]
choice=None
#print(sorts)

while choice !="0":
    print(""" Enter Any Choice
          0 - Exit
          1 - Show Scores
          2 - Add a Score
          3 - Delete a Score
          4 - Sort Score
          """ )
    choice=input("Enter your choice ")
    if choice=="0":
        print("We are exiting the game 'Good Bye!!'")
    elif choice=="1":
        print("High Scores")
        for score in sorts:
            print(score,end="   ")
    elif choice=="2":
        print("Add New Score  ")
        NewScore=int(input("Enter New Score "))
        sorts.append(NewScore)
    elif choice=="3":
        print("Delete a Score")
        RemoveScore=int(input("Enter Score to be Removed"))
        sorts.remove(RemoveScore)
    elif choice=="4":
        print("Score Sort")
        sorts.sort(reverse=True)
        print(sorts)
        
    else:
        print("No valie choice")
    
    



    
    

        
    


