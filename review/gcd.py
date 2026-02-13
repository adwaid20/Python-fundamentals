a=int(input("enter no one"))
b=int(input("enter no second"))
for i in range (1,min(a,b)+1):
    if a%i==0 and b%i==0:
        h=i
print(h)