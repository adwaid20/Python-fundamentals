class employee():
    def __init__(self,name,company):
        self.name=name
        self.company=company
        print(f"employee:{self.name} ,company name:{self.company}")

    
class Devolper(employee):
    def __init__(self, name, company,lang,salary):
        super().__init__(name,company)
        self.lang=lang
        self.salary=salary
        print(f"{self.name} is a {self.lang} devolper with salary{self.salary}\n")

class Manager(employee):
    def __init__(self, name, company,pos,salary):
        super().__init__(name, company)
        self.pos=pos
        self.salary=salary
        print(f"{self.pos} has {self.salary} slary\n")

c=Devolper("adwaid","ust","python",35000)
m=Manager("arun","ust","manager",35000)
    