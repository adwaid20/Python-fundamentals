import json
print("welcome to lonexh quiz")
print()
list1= [
  {
    "ques": "what is my name",
    "options": {
      "a": "adwaid",
      "b": "adil",
      "c": "echu",
      "d": "aloshi"
    },
    "answer": "a"
  },
  {
    "ques": "where am i from",
    "options": {
      "a": "vadakara",
      "b": "kannur",
      "c": "chengannur",
      "d": "calicut"
    },
    "answer": "a"
  }
]
with open("q.json","w") as f:
    json.dump(list1,f)

def load():
    with open("q.json","r") as f:
        list1=json.load(f)
    for questions in list1:
        print(questions["ques"])
        for i,j in questions["options"].items():
            print(f"{i} : {j}")
        n=input("enter answer : ")
        if n==questions["answer"]:
            print()
            print("correct answer")
            print()
            print("your next question is")
        else:
            print("wrong answer., poyi padichitt vaa")
            print()
        



load()