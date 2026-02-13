a=int(input("enter no to check"))
if a<2:
    print("not prime")
elif a==2 or a==3:
    print("it is prime")
elif a>2:
    for i in range(2,a):
        if a%i==0:
            print("not prime")
            break
    else:
     print(str(a) + "is prime")

