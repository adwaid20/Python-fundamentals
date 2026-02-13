def fizzBuzz(n):
    for i in range(1,n+1):
        if i%3==0:
            print("fizz")
        elif i%5==0:
            print("buzz")
        elif i%3==0 and n%5==0:
            print("fizzBuzz")
        else:
            print(i)
n=int(input("Enter a no:"))
fizzBuzz(n)