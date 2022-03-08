class emp:
    def __init__ (self,empid,name,salary,address):
        self.empid = empid
        self.name = name
        self.salary = salary
        self.add = address
class teach(emp):
    def __init__ (self,empid,name,salary,address,dept,sub):
        emp. __init__ (self,empid,name,salary,address)
        self.dept = dept
        self.sub = sub
        
    def display(self):
        print ("\nEmployee Id: ",self.empid,"\nName: ",self.name,"\nSalary: ",self.salary,"\nAddress: ",self.add,"\nDepartment: ",self.dept,"\nSubject: ",self.sub)
        
e = int (input ("Enter the EmpId ") )
n = input ("Enter the Name ")
m = int (input ("Enter the Salary ") )
a = input ("Enter the Address ")
d = input ("Enter the Department ")
s = input ("Enter the Subject ")

ob1 = emp(e,n,m,a)
ob2 = teach(e,n,m,a,d,s)

ob2.display()
