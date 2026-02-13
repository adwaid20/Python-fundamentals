def vowels(a):
    v="aeiou"
    count=0
    a=a.lower()
    for ch in a:
        if ch in v:
            count=count+1
    print("no of vowels is ",count)
    
word=str(input("enter the word to check"))
vowels(word)