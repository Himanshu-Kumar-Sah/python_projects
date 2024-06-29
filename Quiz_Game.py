import random
import ast

def questions():
    level = [0,1000,2000,3000,4000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,7500000,10000000,70000000]
    cans = 0
    for i in range(0,19):    
        A = random.randint(1,100)
        file = open("C:/Users/91971/NEW VS Code/kbc_questions.txt","r")
        lines = file.readlines()
        file.close()
        line = lines[A - 1]
        question =  ast.literal_eval(line.strip())
        print(f"QUESTION: {question[0]} ")
        print(f"A: {question[1]:<20}             B: {question[2]}")
        print(f"C: {question[3]:<20}             D: {question[4]}")
        Ans = input("Enter the correct option / Quit(Q):")
        if cans == 18:
            print("YOU WON THIS GAME")
            mainmenu()
        if Ans == question[5]:
            print("Correct Answer")
            cans = cans + 1
            print("You have won Rs:",level[cans])
        elif Ans == "Q":
            print("Thank you for playing")
            print("You can go home with Rs:",level[cans])
            mainmenu()
        else:
            print("Wrong Answer")
            print("Correct Answer is :",question[5])
            print("You Lose")
            print("You can go home with Rs:",level[cans])
            mainmenu()
       
    
def mainmenu():
    print("----------- Quiz Game----------------")
    print("-------  Play Game  ------")
    print("----------- EXIT --------")
    for i in range(0,1000):
        Level = input("Play(P) or EXIT : ")
        if Level == "P":
            questions()
        elif Level == "EXIT":
            exit()
        else:
            print("Wrong Input: Try Again")

    
    
mainmenu()
    
