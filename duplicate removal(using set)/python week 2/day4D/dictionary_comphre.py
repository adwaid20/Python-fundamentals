words = ["apple", "banana", "grape", "kiwi", "mango", "pear"]
d={x:"long" if len(x)>4 else "short" for x in words}
print(d)

# d={x:len(x) for x in words}
# print(d)