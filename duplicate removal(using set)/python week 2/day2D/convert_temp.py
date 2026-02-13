n=int(input("for converting celsius to far, press 1 \nfor farenhiet to celsius, press 2"))
t=float(input("enter temperature"))
def fun(a,m):
    if m==1:
        f=(a*(9/5))+32
        return print(f,"F")
    elif m==2:
        c=((a-32)*5)/9
        return print(c,"C")
    else:
        return print("invalid selection")
fun(t,n)