a=str(input("enter first word"))
b=str(input("enter second word"))
a=a.lower()
b=b.lower()
if sorted(a)==sorted(b):
    print("it is anagram")
else: 
    print("it is not anagram")