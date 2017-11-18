# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 13:39:16 2017

@author: FPaulraj
"""

def instructions():
    print("""
          Welcome to the greatest intellectual challenge of all time; Tic-Tac-Toe.
          This will be a showdown between your human brain and my silicon processor.
          
          You will make your move known by entering a number, 0-8.  The number will 
          correspond to the board position as illustrated:
                          0  |  1  |  2  
                          -------------
                          3  |  4  |  5
                          -------------
                          6  |  7  |  8
         """
         )
def display(message):
    print(message)
    
def give_me_five():
    five=5
    return five

def any_yes_no(question):
    response=None
    while response not in ("y","n"):
        response = input(question).lower()
        return response
 # main
print("Here are the instructions to the Tic-Tac-Toe game:")
instructions()
msg=display("This calls display function")
fi_number=give_me_five()
print("This just returns the funciton",fi_number,"\n")
y_n=any_yes_no("Enter the 'n' or 'y'\n")
print("Thankis for Entering ", y_n)

input("enter any key to exit")


