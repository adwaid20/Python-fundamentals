d={}
n=int(input("enter no of key value pairs to be stored :"))
for i in range (0,n):
    key=input(f"enter key -{i+1} ")
    value=int(input(f"enter mark of {key} "))
    d[key]=value
#to save a dictionary according to the user(a single dictionary with multiple key-value pair)
m=max(d, key=d.get)
print(f"the topper is {m} and the mark scored is {d[m]}")