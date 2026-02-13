data=(input("write the contents to file:"))
with open("userData.txt",'w') as f:
    f.write(data)
with open("userData.txt",'r') as f:
    contents=f.read()
    print("file contents:",contents)
    