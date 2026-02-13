def prime(n):
    if n<2:
        print("it is not prime")
    else:
        for i in range (2,n):
            if n%i==0:
                print("its is not prime")
                break
        else:
            print("it is prime")

a=int(input("enter to check prime"))
prime(a)