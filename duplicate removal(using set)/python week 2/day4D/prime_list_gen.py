n=int(input("enter range till prime to be printed"))
li=[x for x in range(2,n) if all(x%i!=0 for i in range(2,x) )] #all enda use akunne vechal,oru iteration kodukua(for loop pole) athile ella iterationum true  annel mathram value return cheyum
print(li)   #prints x only if all values are true