def fun(n):
    d={}
    total=0
    for i in range(n):
        key=input("enter item name")
        value=int(input("enter the rate"))
        d[key]=value
    for v in d.values():
        total=total+v
    return total  
m=int(input("enter no of items"))
print("the total bill is ",fun(m))