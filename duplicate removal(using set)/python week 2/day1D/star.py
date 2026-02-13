n=int(input("enter no of rows required"))
for i in range(n):
    print(" "*(n-i),end="")
    print(" *"*i)
for i in range(n,-1,-1):
    print(" "*(n-i),end="")
    print(" *"*i)