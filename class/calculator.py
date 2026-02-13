class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def addition(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def multi(self):
        return self.a*self.b
    def div(self):
        if self.b==0:
            print("invalid")
        else:
            return self.a/self.b

s=Calculator(10,20)
print(s.addition())