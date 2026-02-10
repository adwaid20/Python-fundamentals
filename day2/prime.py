def prime():
    if n<=1:
        print("Not prime")
    else:
        for i in range(2,n):
            if n%i==0:
                print("Not prime")
                break
        else:
            print("prime")
n=int(input("Enter a no:"))
prime()