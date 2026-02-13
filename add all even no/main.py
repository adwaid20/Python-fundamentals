list1=list(map(int,input("enter number of list").split(" ")))
sum=0
for i in list1:
    if i%2==0:
        sum=sum+i
print(sum)