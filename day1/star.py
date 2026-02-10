# n=6
# for i in range(1,n):
#     print(" "*(n-i),end="")
#     print("*"*(i))
n=6
for i in range(1,n):
    for j in range(i):
        print("* ",end="")
    print()