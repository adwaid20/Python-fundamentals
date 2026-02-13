n=int(input("enter no of contacts you want to save"))
d=[]
class contact:
    def __init__(self,name,number):
            self.name=name
            self.number=number
    def __repr__(self):
          return f"{self.name}:{self.number}"

    
#ivide namale list il oro object ayitt aan append cheyunne so call cheyumbo
#ch.name allel ch.number enne okeye specify cheyanam(for loop allel iterations il)

for i in range (n):
      name=str(input("enter name"))
      number=input("enter number")
      if any(c.name.lower()==name.lower() for c in d):
           print("contact alresdy exists")
      else:
       c=contact(name,number)
       d.append(c)
print(d)


while True:
    m=int(input("enter what to do:\n 1 for contact searching \n 2 to save new contact \n 3 for editing contact"))
    
    if m==1:
        ch=str(input("enter name to be searched"))
        for c in d:
            if c.name==ch:
                print(c)
            else:
                print("name not present")
    
    if m==2:
        q=int(input("enter no of contacts you want to save"))
        for i in range (q):
            name=str(input("enter name"))
            number=input("enter number")
            if any (ch.name.lower()==name.lower() for ch in d):
                print("contact name already exist")
            else:
                c=contact(name,number)
                d.append(c)
        print(d)
    
    if m==3:
        ch=str(input("enter name to be searched"))
        for c in d:
            if c.name.lower()==ch.lower():
                num=input("enter new number")
                c.number=num
                break
        else:
            print("do not exist in contact")
        print(d)

    with open("save.txt","a") as f:
        for c in d:
            f.write(f"{c.name}:{c.number}\n")