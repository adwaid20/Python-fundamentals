class student:
    school="makbig"
    place="kzh"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def disp(self):
        print(f"{self.name}\n{self.age}\n{student.school}")
    
s1=student("adwaid",23)
s2=student("echu",22)

s1.disp()
s2.disp()
        