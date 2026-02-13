n=str(input("enter a string"))
freq={}
for ch in n:
    freq[ch]=freq.get(ch,0)+1
print(freq)