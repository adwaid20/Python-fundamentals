class invalidage(Exception):
    pass
n=input("enter your age")
try:
    n=int(n)
    if n<18:
        raise invalidage  #invalidage enne parane oru error njan custom indaki vachu
    else:
        print("age is valid")
except invalidage:      #ivide njan athe call cheyithu
    print("age invalid") 
except ValueError:
    print("enter a number as age")
finally:
    print("done")