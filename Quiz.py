questions=  [
                {         
                "prompt":"From the options below, Choose one of seven wonders of the world?",
                "options":["a. Effiel Tower", "b. Mount Everest","c. Ashok Pilar","d. RedFort"],
                "answer": "a"
                },
                {
                    "prompt":"Name the fastest Marathon Athelete who acquired Guiness world record?",
                    "options":["a. Sania Mirza", "b. Virat Kohli", "c. Abel Anton", "d. Usain Bolt"],
                    "answer":"d"
                        
                },
                {
                    "prompt":"In which country you can find Sydney Opera house?",
                    "options":["a. America","b. England","c. Germany","d. Australia"],
                    "answer":"d"
                },
                {
                    "prompt":" What has a thumb and four fingers but is not a hand?",
                    "options":["a. Middle Finger","b. Index finger","c. Thumb","d. Palm"],
                    "answer": "c"
                }]
def run_quiz(questions):
    score=1
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer=input("Enter Your Answer (a,b,c,d):")
        if(answer==question["answer"]):
            print(f"Congragulations!! Your answer was correct and Your score is {score}")
            score+=1
        else:
            score-=1
            print(f"oops!! wrong answer!! and correct answer is {question["answer"]}.Your score is {score}")
    print(f"You have obtained {score} out of {len(questions)} questions correct")
run_quiz(questions)


