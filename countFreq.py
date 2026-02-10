# f=open("hello rishana.txt")
# text=f.read().split()
# freq={}
# for ch in text:
#     if ch in freq:
#         freq[ch]+=1
#     else:
#         freq[ch]=1
# print(freq)
# f.close()

with open("hello rishana.txt") as f:
    words=f.read().split()
freq={w:words.count(w) for w in set(words)}
print(freq)
