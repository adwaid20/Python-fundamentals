class book:
    book="librarys"
    def __init__(self,name,author):
        self.name=name
        self.author=author
    def disp(self):
        return print(f"{self.name} is written by {self.author}")
b1=book("HP","jk")
b2=book("sita","amish")
b1.disp()
b2.disp()