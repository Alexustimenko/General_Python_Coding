#-----------------------------
def new_game():
    guesses=[]
    correct_guesses=0
    question_num=1
    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess=input("Enter (A,B,C or D): ")
        guess=guess.upper()
        guesses.append(guess)
        correct_guesses+=check_answer(questions.get(key),guess)
        question_num+=1
    display_score(correct_guesses,guesses)
#-----------------------------
def check_answer(answer, guess):
    if answer==guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0
#-----------------------------
def display_score(correct_guesses,guesses):
    print("---------------------------")
    print("RESULTS")
    print("---------------------------------")
    print("Answers: ",end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()
    score=int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")
#-----------------------------
def play_again():
    response=input("Do you want to play again? (yes or no) : ")
    response=response.upper()
    if response == "YES":
        return True
    else:
        return False
#-----------------------------
questions={
    " When you see >>> inside IDLE, it means that: ":"B",
    "130+125+191 = ":"C",
    "300-(150*2) = ":"D",
    "Which function displays a message on the screen in Python?":"B",
    "Who developed Python Programming Language?":"C",
    "Which of the following is the correct extension of the Python file?":"C",
    "Which is the correct operator for power(xy)?":"B",
    "What is the output of print 0.1 + 0.2 == 0.3?":"B",
    "What is the type of inf?": "C",
    "What is the output of print 9//2 ? ":"D",
    "What is a correct syntax to output Hello World in Python?":"A",
    "How do you insert COMMENTS in Python code?":"C",
    "What word is used to create function in Python? ":"B",
    "Which method can be used to remove any whitespace from both the beginning and the end of a string?":"A",
    "Which method can be used to return a string in upper case letters?":"B"
}
options=[["A.Python is upset","B.Python is waiting for you to give it some instructions","C.An error has occurred","D.Your computer is having an existential crisis"],
         ["A.10000021","B.154785","C.446","D.364"],
         ["A.697","B.548","C.150","D.0"],
         ["A.p","B.print","C.prt","D.prnt"],
         ["A.Elon Musk","B.Alex Python","C.Guido van Rossum","D.Bill Gates"],
         ["A.ptn","B.pyth","C.py","D.pyn"],
         ["A.%","B.**","C.//","D. */"],
         ["A.true","B.false","C.error","D.++++++++++"],
         ["A.int","B.boolean","C.float","D.string"],
         ["A.4","B.2.5","C.0","D.error"],
         ["A.print()","B.prt()","C.p()","D.prtn()"],
         ["A.^^","B.//","C.#","D.*/"],
         ["A.func","B.def","C.f","D.fnctn"],
         ["A.trim()","B.cut()","C.scis()","D.cutt()"],
         ["A.UPPERC","B.upper","C.case","D.uppl"]]
new_game()
while play_again():
    new_game()
print("Byeeeeeeeeeeeeeeeeeeeee!")