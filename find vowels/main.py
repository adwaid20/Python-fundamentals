a=input("""enter the word
""")
v="aeiouAEIOU"
count=0
for ch in a:
   if ch in v:
    count+=1

print(count)

