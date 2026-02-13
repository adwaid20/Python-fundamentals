a = set(map(int, input("enter set 1 with comma").split(",")))
b=set(map(int,input("enter set 2 with comma").split(",")))

if a==b:
    print("a and b is the same set")
elif a<b:
    print("a is subset of b")
elif b<a:
    print("b is subset of a")