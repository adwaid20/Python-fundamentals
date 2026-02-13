d={}
n=int(input("enter total no students to be entered"))
for i in range (n):
    key=input("enter student name : ")
    value=input(f"enter student {key} mark : ")
    d[key]=value
print(d)
while True:
    print("""choose what procedure to continue
1.Show topper
2.edit mark of a student
3.add new student
4.delete a student
5.show all students
6.delete all and start new\n""")

    c=int(input("enter ur choice :- "))
    if c==1:
        topper=max(d, key=d.get)
        print(f"the topper is {topper} and his mark is {d[topper]}")
    elif c==2:
        name=input("which students mark is to be corrected")
        if name in d:
            updatedmark=input(f"enter updated mark for {name} ")
            d[name]=updatedmark
            print("the updated marklist is ",d)
        else:
            print("the entered name is not in the log")
    elif c==3:
        nn=int(input("enter no. of new students to be entered in the log"))
        for i in range (nn):
            key=input(f"enter the name of the student {i+1}")
            value=int(input(f"enter the mark of {key}"))
            d[key]=value
        print(f"the updated list is {d}")
    elif c==4:
        de=input("enter the name to be deleted")
        if de in d:
            d.pop(de)
        else:
            print("u have not enetered a valid name")
        print(f"the new list is {d}")
    elif c==5:
        print(d.keys())
    elif c==6:
        print("deleteing the existing dictionary and starting new")
        d.clear()
    else:
        print("u have entered an invalid choice")







