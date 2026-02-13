import json

def addtask():
    try:
        m=int(input("enter no of task to do"))
    except ValueError:
        return print("invalid input")
    list1=[]
#check any existing task present

    try:
        with open("task.json","r") as f:
            list1=json.load(f)
            print("the exsiting tasks are")
            for i,task in enumerate(list1,start=1):
                status="completed" if task['done'] else "not completed"
                print(f"{i} : {task['task']} : {status}")
    except FileNotFoundError:
        print("No existing task file found or file is invalid. Starting fresh.")
#add new task  
    print
    for i in range(m):
        n=str(input("enter the task to do"))
        t={'task':n, 'done':False}
        list1.append(t)

    # print(list1)

#save updated tasks
    with open("task.json","w") as f:
        json.dump(list1,f)
    

    with open ("task.json","r") as f:
            list1=json.load(f)
    for i,task in enumerate(list1,start=1):
            status= "completed" if task['done'] else "not completed"
            print(f"{i} : {task['task'] }  : {status} ")




def listtask():
    with open("task.json","r") as f:
        list1=json.load(f)
        print("The task to be completed are :")
        for i,task in enumerate(list1,start=1):
            status="d" if task['done'] else "not d"
            print(f"{i} : {task['task']}  {status}") #prints the value of the dictionary , 'task' is the key name
            print( )
#if completed true

def taskdone():
    with open("task.json","r") as f:
        list1=json.load(f)
        m=str(input("enter completed task"))
        for task in list1:
            if task['task']==m:
                task['done']=True #here we changed the value by calling the value of second item of the same dict within theif loop itself
        with open("task.json","w") as f:
            json.dump(list1,f)
        print("The updated list is:")
        for i,task in enumerate(list1,start=1):
            status="completed" if task['done'] else "not completed" #also important a new methrod to mark the status in a single line
            print(f"{i} : {task['task']}  {status}") #prints the value of the dictionary , 'task' is the key name
            print( )



#remove a task
def remove():
    with open("task.json","r") as f:
        list1=json.load(f)

    r=str(input("enter the task to be removed"))

    for i,task in enumerate(list1):
        if task['task']==r:
            list1.pop(i)
            break
    else:
        print("no such task in the list")
        


    with open("task.json","w") as f:
        json.dump(list1,f)
    print("the updated todo is")
    for i,task in enumerate(list1,start=1):
        status="completed" if task["done"] else "not completed"
        print(f"{i} : {task['task']} : {status}")
        print()
#         for i,line in enumerate(f,start=1):
#             task=json.loads(line)
#             if task['task']==r:
#                 task.pop(i)

print("WELCOME TO TODO")
while True:
    select=int(input("enter what to do : \n1 for entering task \n2 for viewing all tasks \n3 for marking done to a completed task \n4 for removing a task"))
    if select==1:
        addtask()
    elif select==2:
        listtask()
    elif select==3:
        taskdone()
    elif select==4:
        remove()
