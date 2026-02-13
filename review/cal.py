# a=int(input("enter number 1"))
# b=int(input("enter no 2"))
# def calculator(a,b):
#     c=int(input("which operation to perform" \
#     "1 for addition" \
#     "2 for multi"))
#     if c==1:
#        return print(a+b)
#     elif c==2:
#         return print(a*b)
# calculator(a,b)













a=int(input("enter number one"))
b=int(input("enter number second"))
def calc(a,b):
    c=int(input("1 for addition\n2 for multi"))
    if c==1:
        return print(a+b)
    elif c==2:
        return print(a*b)
calc(a,b)