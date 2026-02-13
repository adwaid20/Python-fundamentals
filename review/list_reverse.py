a=list(input("enter list").split(","))
print(a)
rev=[]
for i in a:
    rev=[i]+rev
print(rev)