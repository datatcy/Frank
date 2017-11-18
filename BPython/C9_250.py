# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 20:52:14 2017

@author: FPaulraj
"""
"""
class Player(object):
    def blast(self,enemy):
        print("The player blasts an enemy \n")
        enemy.die()
class Alian(object):
    def die(self):
        print("The alian gasps and says , Oh , this is it,.  This is the big one,\n"\
              "Yes, its getting dark now.  Tell my 1.6 million larvae that i loved them\n")
# Main
hero=Player()
invader=Alian()
hero.blast(invader)
"""
class EmpInfo(object):
    def __init__(self,emp_num,emp_name):
        print("Employe numer is :")
        self.emp_num=emp_num
        self.emp_name=emp_name
    def __str__(self):
        return self.emp_num, self.emp_name
    def emp(self):
        print("Employee Number : ",self.emp_num, "   ",self.emp_name)
        #self.emp_num=emp_num
empinem=int(input("Enter Employee Number :\n"))
empiname=input("Enter Employee Name :\n")
empin=EmpInfo(emp_num=empinem,emp_name=empiname)
empin.emp()
print(empin.emp_num)
#empin.emp()