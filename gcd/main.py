a=int(input("enter the first number"))
b=int(input("enter second number"))
gcd=0
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        gcd=i
print(gcd)