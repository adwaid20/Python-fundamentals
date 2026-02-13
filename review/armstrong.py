n=int(input("enter a number to check armstrong"))
temp=n
p=len(str(n))
total=0
while temp>0:
    d=temp%10
    total+=d**p
    temp=temp//10

if total==n:
    print("it is armstrong")
else:
    print("not armstrong")