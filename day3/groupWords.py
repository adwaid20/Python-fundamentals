words=["apple","pineapple","orange"]
group={}
for i in words:
    length=len(i)
    if length not in group:
        group[length]=[]
    group[length].append(i)
for length,group in group.items():
    print(f"{length} characters in {group}")