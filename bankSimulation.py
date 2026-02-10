class Account:
    bal=0
    def __init__(self,accno,name,bal):
        self.accno=accno
        self.name=name
        self.bal=bal
    def deposit(self,amount):
        self.bal+=amount
        print(f"{amount} to be deposited,new balance:{self.bal}")
        self.filelog(f"{amount} deposited")

    def withdraw(self,amount):
        if amount>self.bal:
            print("insufficient balance")
            self.filelog(f"{amount} failed to withdraw")
        else:
            self.bal=self.bal-amount
            print(f"{amount} to be widthdraw,new balance{self.bal}")
            self.filelog(f"{amount} withdrawed")

    def checkBalance(self):
            print(f"Balance{self.bal}")
    def filelog(self,message):
         with open("bank_log.txt",'a') as f:
              f.write(f"{self.accno}-{self.name}-{message}\n")


accno=int(input("Enter the account no:"))
name=(input("Enter the account holder name:"))
bal=int(input("Enter the current bank amount:"))
obj=Account(accno,name,bal)
dep=int(input("Enter the amount to be deposited:"))
obj.deposit(dep)
c=int(input("Enter the amount to be withdraw:"))
obj.withdraw(c)
obj.checkBalance()
