class student:
    school="makbig"
    place="kozhikode"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def disp(self):
        print(f"{self.name}\n{self.age}\n{student.school}")

n=int(input("how many students to enter"))
stu=[]
for i in range(n):
    name=input("enter name")
    age=int(input("enter age"))
    s=student(name,age)
    stu.append(s)

for s in stu:
    s.disp()