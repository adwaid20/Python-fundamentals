class circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        self.a=3.14*(self.r**2)
        return self.a
    def cir(self):
        self.c=3.14*2*self.r
        return self.c
    
radius=circle(2)
print(radius.area() , radius.cir())