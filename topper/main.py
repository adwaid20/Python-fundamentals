d={}
n=int(input("enter  no of students names to be entered"))
for i in range (n):
    key=input("enter student name")
    value=int(input(f"enter {key}'s marks"))
    d[key]=value
m=max(d.values())
print("the highest mark is ",m)
topper=max(d, key=d.get)
print(topper)