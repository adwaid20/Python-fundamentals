d=input("enter no")
try:
    d=float(d)
    f=10/d
    print(f"{f:.2f}")
except ZeroDivisionError:
    print("not divible by zero")
except ValueError:
    print("not an interger")
finally:
    print("done")