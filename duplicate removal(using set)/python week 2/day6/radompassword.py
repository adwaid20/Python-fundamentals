import random
import string
q=[]
l=int(input("enter length of the password"))
s=string.printable
ch=string.ascii_letters+string.digits
for i in range (l):
    p=random.choice(ch)
    q.append(p)
    r="".join(q)
print(r)