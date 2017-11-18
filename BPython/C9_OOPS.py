
class EmpInfo(object):
    def __init__(self,emp_num,emp_name,emp_title,emp_exp,emp_salary):
        self.emp_num=emp_num
        self.emp_name=emp_name
        self.emp_title=emp_title
        self.emp_exp=emp_exp
        self.emp_salary=emp_salary
    def __str__(self):
        return  self.emp_num,self.emp_name,self.emp_title,self.emp_exp,self.emp_salary        
    def emp(self):
        print("Employee Number : ",self.emp_num,end="\n")
        print("Employee Name :",self.emp_name,end="\n")
        print("Employee Disignation :",self.emp_title,end="\n")
        print("Employee Experience :",self.emp_exp,end="\n")
        print("Employee Salary :",self.emp_salary,end="\n")
    
    def bonus(self):
        
        if self.emp_exp in range(3,5):
            print("Enployee Bonus ",self.emp_salary * 5)
        elif self.emp_exp in range(5,10):
            print("Employee Bonus ",self.emp_salary * 10)
        else:
            print("Employee bonum :",self.emp_salary *15)

EmpNum=int(input("Enter Employee Number : "))
EmpName=input("Enter Employee Name :")
EmpTitle=input("Enter Employee Title :")
EmpExp=int(input("Enter Employee Experience :"))
EmpSalary=int(input("Enter Employee Salary : "))

empin=EmpInfo(emp_num=EmpNum,emp_name=EmpName,emp_title=EmpTitle,emp_exp=EmpExp, emp_salary=EmpSalary)
empin.emp()
empin.bonus()
