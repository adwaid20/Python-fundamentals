n=int(input("enter no of students to enter"))
d={}
for i in range(n):
    key=str(input("enter student name"))
    value=str(input("enter student mark"))
    d[key]=value
for key,values in d.items():
    print(f"the dictionarys is {key}={values}")
