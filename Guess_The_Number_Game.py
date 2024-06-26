import random

def guesseasy():
    chance = 5 
    A = random.randint(1,10)
    print("Level:- EASY : Range: 1 to 10 ")
    print("Chances:",chance)
    for i in range(1,6):
        num = int(input("Enter the number : "))
        if num == A:
            print("CORRECT GUESS :) - ", A)
            D = input("PLAY AGAIN OR Main Menu - (P/M): ")
            if D == "P":
                guesseasy()
            elif D == "M":
                mainmenu()
        elif num > A:
            print("WRONG GUESS :( - Yours Number is Greater")
            chance = chance - 1
            print("Left Chances: ", chance)
            if chance == 0:
                print("YOU LOSE")
                D = input("PLAY AGAIN OR Main Menu - (P/M): ")
                if D == "P":
                    guesseasy()
                elif D == "M":
                    mainmenu()
        elif num < A:
            print("WRONG GUESS :( - Yours Number is Smaller")
            chance = chance - 1
            print("Left Chances: ", chance)
            if chance == 0:
                print("YOU LOSE")
                D = input("PLAY AGAIN OR Main Menu - (P/M): ")
                if D == "P":
                    guesseasy()
                elif D == "M":
                    mainmenu() 
            
def guessmedium():
    chance = 10 
    A = random.randint(1,50)
    print("Level:- MEDIUM : Range: 1 to 50 ")
    print("Chances:",chance)
    for i in range(1,11):
        num = int(input("Enter the number : "))
        if num == A:
            print("CORRECT GUESS :) - ", A)
            D = input("PLAY AGAIN OR Main Menu - (P/M): ")
            if D == "P":
                guessmedium()
            elif D == "M":
                mainmenu() 
        elif num > A:
            print("WRONG GUESS :( - Yours Number is Greater")
            chance = chance - 1
            print("Left Chances: ", chance)
            if chance == 0:
                print("YOU LOSE")
                D = input("PLAY AGAIN OR Main Menu - (P/M): ")
                if D == "P":
                    guessmedium()
                elif D == "M":
                    mainmenu() 
        elif num < A:
            print("WRONG GUESS :( - Yours Number is Smaller")
            chance = chance - 1
            print("Left Chances: ", chance)
            if chance == 0:
                print("YOU LOSE")
                D = input("PLAY AGAIN OR Main Menu - (P/M): ")
                if D == "P":
                    guessmedium()
                elif D == "M":
                    mainmenu()

def guesshard():
    chance = 20 
    A = random.randint(1,100)
    print("Level:- HARD: Range: 1 to 100 ")
    print("Chances:",chance)
    for i in range(1,21):
        num = int(input("Enter the number : "))
        if num == A:
            print("CORRECT GUESS :) - ", A)
            D = input("PLAY AGAIN OR Main Menu - (P/M): ")
            if D == "P":
                guesshard()
            elif D == "M":
                mainmenu()
        elif num > A:
            print("WRONG GUESS :( - Yours Number is Greater")
            chance = chance - 1
            print("Left Chances: ", chance)
            if chance == 0:
                print("YOU LOSE")
                D = input("PLAY AGAIN OR Main Menu - (P/M): ")
                if D == "P":
                    guesshard()
                elif D == "M":
                    mainmenu()
        elif num < A:
            print("WRONG GUESS :( - Yours Number is Smaller")
            chance = chance - 1
            print("Left Chances: ", chance)
            if chance == 0:
                print("YOU LOSE")
                D = input("PLAY AGAIN OR Main Menu - (P/M): ")
                if D == "P":
                    guesshard()
                elif D == "M":
                    mainmenu() 



def mainmenu():
    print("----------------------  GUESS THE NUMBER GAME  ---------------------------")
    print("-------  Choose Level ------")
    print("----------- EASY --------")
    print("---------- MEDIUM -------")
    print("----------- HARD --------")
    print("----------- EXIT --------")
    for i in range(0,1000):
        Level = input("Enter Level (E/M/H) or EXIT : ")
        if Level == "E":
            guesseasy()
        elif Level == "M":
            guessmedium()
        elif Level == "H":
            guesshard()
        elif Level == "EXIT":
            exit()
        else:
            print("Wrong Input: Try Again")



# main 
mainmenu()
