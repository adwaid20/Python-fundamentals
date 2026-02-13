class AgeTooYoungError(Exception):
    def __init__(self,age):
        self.age=age
        super().__init__(f"Age {age} is too young to vote")

def age_check(age):
    if age<18:
        raise AgeTooYoungError(age)
    else:
        print("Eligible to vote")
try:
    age=int(input("Enter your age:"))
    age_check(age) 
except AgeTooYoungError as e:
    print("caught an error:",e)

   