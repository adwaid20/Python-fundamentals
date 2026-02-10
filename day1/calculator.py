a=int(input("Enter first no:"))
b=int(input("Enter second no:"))
print("1.add\n2.subtract\n3.multipy\n4.division")
choice=int(input("Enter a choice:"))
def calculator():
    if choice==1:
        n=a+b
    elif choice==2:
        n=a-b
    elif choice==3:
        n=a*b
    elif choice==4:
        n=a//b
    else:
        n="Invalid choice"
    return n
print(calculator())
