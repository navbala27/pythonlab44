class Bank:
    def __init__ (self,accno,name,type,bal):
        self.no = accno
        self.name = name
        self.type = type
        self.bal = bal
    
    def deposit(self):
        amount = int (input ("Enter the Amount"))
        self.bal += amount
        print (amount," Succesfully Deposited")
    
    def withdraw(self):
        cash = int (input ("Enter Money"))
        if self.bal >= cash:
            self.bal-=cash
            print(cash," Succesfully Withdrawn")
        else:
            print("Insufficient Balance")
            
    def display(self):
        print("\nAccount No: ",self.no,"\nName: ",self.name,"\nType: ",self.type,"\nBalance: ",self.bal)
        

ob = Bank(1014,'Bala','Savings',1500)

ob.deposit()
ob.withdraw()
ob.display()
