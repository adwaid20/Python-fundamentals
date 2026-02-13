a=int(input("enter a number to check prime :"))
if a<2:
 print("the number is not prime")
elif a>=2:
 for i in range (2,a):#inside elif conditio
     if a%i==0:# inside for loop
        print("it is not prime")
        break # to not repeat the loop
 else: #outside for loop but inside elif condition
        print("it is prime")
