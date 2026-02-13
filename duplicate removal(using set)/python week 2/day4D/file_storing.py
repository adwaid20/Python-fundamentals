# u=str(input("enter user name"))
# a=int(input("enter your age"))
# with open("text1.txt","w") as f:
#     f.write(f"{u} : {a}")
# print("user data saved")




#to append

u=str(input("enter user name"))
a=int(input("enter your age\n"))
with open("text1.txt","a") as f:
    f.write(f"{u} : {a}")
print("user data saved")


