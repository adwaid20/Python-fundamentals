score={"alan":[20,30,46],
               "lex":[40,56,78],
               "dyan":[37,32,98]}
print(score)
new_score=int(input("Enter new score for alan:"))
score["alan"].append(new_score)
print("new score",score)

avg=sum(score["lex"])/len(score["lex"])
print("Average of lex",avg)
top=max(score,key=score.get)
print("topper is:",top)