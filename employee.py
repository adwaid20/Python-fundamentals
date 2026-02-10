class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def role(self):
        return "emp"
class Manager(employee):
    def role(self):
        return "manager"
class Developer(employee):
    def role(self):
        return "dev"
e1=Manager("anu",50000)
e2=Developer("minu",40000)
print(e1.name,e1.role())
print(e2.name,e2.salary)