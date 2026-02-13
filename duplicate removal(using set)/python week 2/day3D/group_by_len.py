# lis=["apple","app","lan","hi","qwert","hai"]
# d={}
# for value in lis:
#     key=len(value)
#     if key in d:
#         d[key].append(value) #value.append(word)  ivide sherik d[key] enne vechal value aan, value ude list il aan append aavine
#     else:                    #appo value kalude list (putjiya value vanal list undakan namale thaye else il code akitt ind)
#         d[key]=[value]       #ivide and value kalude list il ipo vanne value add cheyan parayum(like only if key equal aanel)
    
# print(d)















li=["sdfds","edede","edee","aw","as"]
d={}
for words in li:
    key=len(words)
    if key in d:
        d[key].append(words) #ivide d.vales use akila karanam athe list alla just oru viewing object ayitt aan tharua
    else:                       #but list ayi thanalum (adhyame list akua*code1) ivide aa sepcific key ile list il thanne venam aa specific value allel string append aavan so d[key].append(i)
        d[key]=[words]  #*code1
print(d)