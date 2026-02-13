n=int(input("enter number limit"))
for i in range(n):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%5==0:
        print("buzz")
    elif i%3==0:
        print("fizz")  
    else:
        print(i)