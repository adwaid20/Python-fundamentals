def division(a,b):
    try:
        result=a/b
        return result
    except ZeroDivisionError:
        return "Error:division not possible by zero!"
a=int(input("enter 1st no:"))
b=int(input("enter 2nd no:"))
print("result:",division(a,b))