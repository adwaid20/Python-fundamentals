a=int(input("enter number one"))
b=int(input("enter number two"))
def addition():
    return a+b
def sub():
    return a-b
def multi():
    return a*b
def div():
    return a/b
c=int(input("enter a chice:\n 1 for add \n 2 for sub"))
if c==1:
    print(f"addition sum is {addition()}")
elif c==2:
    print(sub())