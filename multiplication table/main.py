a=int(input("multiplication table of num1 : "))
b=int(input("multiplication table of num2 : "))

for i in range(1,11):
    print(f"{str(a) + "x" + str(i) + "=" + str(a*i).ljust(8)}"  f"{b}x{i}={b*i}")
    #arranged both table in rows use string type for one and f"{}" placeholder format for other
    #used l.just<4 which is left align and use 8 characters

