n=int(input("enter the number to check:"))
def fun(a):
    if a<2:
        print("it is not a prime number")
    else:
        for i in range(2,a):
            if a%i==0:
                print("it is not prime")
                break
        else:
            print("it is a prime number")
fun(n)