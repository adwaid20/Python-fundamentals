n=int(input("enter no of input u want to give"))
d={}
for i in range(n):
    key=input("enter key ")
    value=input("enter value")
    d[key]=value
print(d)
m=max(d,key=d.get)
print(m,d[m])













# n=int(input("enter no of slot required"))
# d={}
# for i in range (n):
#     key=input("enter key")
#     value=input("entern value")
#     d[key]=value
# m=max(d,key=d.get)
# print(m,d[m])
