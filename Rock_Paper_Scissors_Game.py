import random

def cinout():
    cin = random.randint(1,3)
    if cin == 1:
        cout = "ROCK"
    elif cin == 2:
        cout = "PAPER"
    elif cin == 3:
        cout = "SCISSORS"
    return cout


def userinput():
    usin = int(input("Enter Yours Choise - (1/2/3): \n 1 - ROCK \n 2 - PAPER \n 3 - SCISSORS \n:-> "))
    if usin == 1:
        usout = "ROCK"
    elif usin == 2:
        usout = "PAPER"
    elif usin == 3:
        usout = "SCISSORS"
    else:
        print("Wrong Choise: Try Again")
        userinput()
    return usout


# def game(N):
    cscore = 0
    usscore = 0
    for i in range(1,N):
        cout = cinout()
        usout = userinput()
        if cout == usout:
            print("Draw")
        elif cout == "ROCK" and usout == "PAPER":
            print("YOU WIN COMPUTER LOOSE")
            usscore = usscore + 1
        elif cout == "PAPER" and usout == "ROCK":
            print("COMPUTER WIN YOU LOOSE")
            cscore = cscore + 1
        elif cout == "ROCK" and usout == "SCISSORS":
            print("COMPUTER WIN YOU LOOSE")
            cscore = cscore + 1    
        elif cout == "SCISSORS" and usout == "ROCK":
            print("YOU WIN COMPUTER LOOSE")
            usscore = usscore + 1
        elif cout == "PAPER" and usout == "SCISSORS":
            print("YOU WIN COMPUTER LOOSE")
            usscore = usscore + 1
        elif cout == "SCISSORS" and usout == "PAPER":
            print("COMPUTER WIN YOU LOOSE")
            cscore = cscore + 1
        if cscore == usscore:
            print("computer score:",cscore,"YOURS score:",usscore)
        elif cscore > usscore:
            print("computer score:",cscore,"YOURS score:",usscore)
        elif cscore < usscore:
            print("computer score:",cscore,"YOURS score:",usscore)

def game(N):
    cscore = 0
    usscore = 0
    for i in range(1,N):
        cout = cinout()
        usout = userinput()
        if cout == usout:
            print("Draw")
        elif cout == "ROCK" and usout == "PAPER":
            print("You win this round 😄")
            usscore = usscore + 1
            print("Computer Score:",cscore,"Yours Score:",usscore)
        elif cout == "PAPER" and usout == "ROCK":
            print("Computer win this round 😭")
            cscore = cscore + 1
            print("Computer score:",cscore,"Yours Score:",usscore)
        elif cout == "ROCK" and usout == "SCISSORS":
            print("Computer win this round 😭")
            cscore = cscore + 1
            print("Computer Score:",cscore,"Yours Score:",usscore)    
        elif cout == "SCISSORS" and usout == "ROCK":
            print("You win this round 😄")
            usscore = usscore + 1
            print("Computer Score:",cscore,"Yours Score:",usscore)
        elif cout == "PAPER" and usout == "SCISSORS":
            print("You win this round 😄")
            usscore = usscore + 1
            print("Computer Score:",cscore,"Yours Score:",usscore)
        elif cout == "SCISSORS" and usout == "PAPER":
            print("Computer win this round 😭")
            cscore = cscore + 1
            print("Computer Score:",cscore,"Yours Score:",usscore)
    if cscore == usscore:
        print("GAME DRAW")   
    elif cscore > usscore:
        print("COMPUTER WINS 😭")
    elif cscore < usscore:
        print("YOU WIN 😄")


def rpsbt():
    game(4)

def rpsbf():
    game(6)

def rpsnrd(N):
    game(N)

def rpsend():
    n = 100**100
    while (1<2)==True:
        game(n)
        


def mainmenu():
    print("---------- Rock__Paper__Scissors__Game -----------")
    print("---------------  Choose_Type  ------------------")
    print("---------------  Best_of_Three  ----------------")
    print("---------------  Best_of_Five  ----------------")
    print("---------------    N Rounds  ----------------")
    print("---------------    Endless     ----------------")
    print("---------------     EXIT       ----------------")
    for i in range(0,1000):
        type = input("BEST of Three/Five/N rounds/Endless (T/F/N/E) or EXIT :")    
        if type == "T":
            rpsbt()
        elif type == "F":
            rpsbf()
        elif type == "E":
            rpsend()
        elif type == "N":
            N = int(input("Enter Number of Rounds You want to play : "))
            rpsnrd(N)
        elif type == "EXIT":
            exit()
        else:
            print("Wrong Input: Try Again")

#MAIN
mainmenu()
