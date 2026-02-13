def quizz():
    score=0
    with open("question.txt",'r') as f:
        for line in f:
            parts=line.strip().split("|")
            question,optn1,optn2,optn3,optn4,answer=parts
            print(question)
            print(f"{optn1}\n{optn2}\n{optn3}\n{optn4}\n")
            userAns=(input("Mark your answer:"))
            if userAns.lower()==answer.lower():
                print("Your answer is Correct")
                score+=1
            else:
                print("Wrong answer")

    print(f"Your final score:{score}")
quizz()

# logfile=()
    # def logFile():
    #     with open("quiz_log.txt",'a') as f:
    #         print(f.write("hi"))