def todo():
    print("Welcome to todo app!")
    print("1.Add task\n2.view task\n3.Delete task\n4.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        with open("hellorishana.txt","a") as f:
            task=(input("Enter your task:"))
            f.write(task)
            print("task added")
    elif choice==2:
        try:
             with open("hellorishana.txt",'r') as f:
                  print("tasks:")
                  print(f.read())
        except FileNotFoundError:
             print("file not found")
    elif choice==3:
        with open("hellorishana.txt","w") as f:
            f.write("")
            print("All task are deleted")
    elif choice==4:
            print("Exiting..")
    else:
        print("invalid choice")
todo()