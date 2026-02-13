a={
    "adwaid":"btech",
    "ashwin":"electronics",
    "aloshi":"cs"
}
b={
    "ad":"python",
    "jk":"mtech",
    "abhay":"banglore"
}

merged=a|b

#to print line by line
for key,value in merged.items():
    print(key,":",value)