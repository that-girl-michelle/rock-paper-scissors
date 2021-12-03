import time
import random

userScore = 0
computerScore = 0

def playerWon():
    global userScore
    userScore += 1
    print("(oh no...)")

def computerWon():
    global computerScore
    computerScore += 1
    print("(HAHA)")

numberOfGames = input("So, how many games would you like to LOSE? (type a number) ")
numberOfGamesInt = int(numberOfGames)

for i in range(numberOfGamesInt):

    print("\n**************") 
    print(f"ROUND {i + 1}")
    print("**************\n") 
    
    userChoice = input("Choose rock, paper or scissors: ")
    while userChoice != "rock" and userChoice != "paper" and userChoice != "scissors":
        print("No monkey business!\n")
        userChoice = input("Choose rock, paper or scissors: ")

    computerActions = ["rock", "paper", "scissors"]
    computerChoice = random.choice(computerActions)

    print(f"Computer chose {computerChoice}. You chose {userChoice}.\n")

    if computerChoice == userChoice:
        print(f"Both of you chose {userChoice}. It's a draw!")

    elif userChoice == "rock":
        if computerChoice == "paper":
            print("Paper wrapped rock. You lost, you fool!")
            computerWon()
        else:
            print("Rock destroyed scissors. You won, good job!")
            playerWon()

    elif userChoice == "paper":
        if computerChoice == "rock":
            print("Paper wrapped rock. You won, congratulations!")
            playerWon()
        else:
            print("Scissors cut paper. You lost, be ashamed!")
            computerWon()

    elif computerChoice == "rock": #user chose scissors
        print("Rock destroyed scissors. You lost, idiot!")
        computerWon()
    else: #user chose scissors, computer chose paper
        print("Scissors cut paper. You won, have some rum! (unless you are underage)")
        playerWon()

    #playAgain = input("Do you dare compete against me one more time? (yes or no) ")
    #if playAgain.lower() != "yes" and playAgain.lower() != "y":
    #    break

print("Congrats (or not)! The current score (you:computer) is *drum roll*...")
for i in range(5):
    print(".")
    time.sleep(0.5)
print(f"{userScore}:{computerScore}")
if userScore > computerScore:
    print("Oh, hey, you- wait. You definitely cheated, that's not fair at all!\nBut, okay, I guess you won then...\n")
elif userScore < computerScore:
    print("I TOLD YOU I WOULD WIN, I ALWAYS DO!!!\nAHAHAHAHAHHAAHHAHAHAHAH-\n")
else:
    print("What?! You got the SAME EXACT SCORE as me? The best rock-paper-scissors PLAYER?!?!?!?\nEh, I won anyway...\n")