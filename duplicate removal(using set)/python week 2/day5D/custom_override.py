class employee:
    def __init__(self,company):
        self.company=company
    def fun(self):
        print(f"{self.company}")
class devolper(employee):
    def __init__(self, company,name):
        super().__init__(company)
        self.name=name
    def fun(self):
        print(f"{self.name} is in {self.company}")
class role(employee):
    def __init__(self,mak,role):
        super().__init__(mak)
        self.role=role
    def fun(self):
        print(f"working in {self.company} and role is {self.role} ")
a=employee("mac")
b=devolper("mak","adwaid")
c=role("mak","python")
a.fun()
b.fun()
c.fun()
