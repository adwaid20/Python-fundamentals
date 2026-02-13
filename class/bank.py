class bank:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance=self.balance+amount
            return self.balance
        else:
            return("invalid amount")
    def withdraw(self,am):
        if am<=self.balance:
            self.balance=self.balance-am
            return self.balance
        else:
            return("not sufficient funds")
        
s=bank("adwiad",1000)

print(s.deposit(500))
print(s.withdraw(1250))
